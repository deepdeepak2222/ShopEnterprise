from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response

from core.constants import ERROR, RESPONSE_KEY, DELETED
from core.exceptions import ShopSerializerValidationError
from core.pagination import StandardResultsSetPagination
from log.log import log_err
from shop_inventory.constants import SHOP_ITEM_TSV_SEARCH_Q
from shop_inventory.filters import ShopItemFilter
from shop_inventory.models import ShopItem
from shop_inventory.serializers import ShopItemSerializer
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ShopItemView(GenericAPIView):
    """
    API Type : POST/PUT/LIST/GET
    API: List/Create/Update/GET shop items
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ShopItemSerializer
    pagination_class = StandardResultsSetPagination
    filterset_class = ShopItemFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        if self.request.query_params.get("q"):
            qs = ShopItem.objects.raw(SHOP_ITEM_TSV_SEARCH_Q % self.request.query_params.get("q"))
            id_list = [q.id for q in qs]
            qs = ShopItem.objects.filter(pk__in=id_list).order_by("-created")
        else:
            qs = ShopItem.objects.all().order_by("-created")
        return qs

    def put(self, request, *args, **kwargs):
        """
        Update shop items
        """
        msg = ERROR
        item_id = kwargs.get("id")
        try:
            instance = ShopItem.objects.get(pk=item_id)
            serializer = self.get_serializer(data=request.data, instance=instance)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except ShopItem.DoesNotExist:
            msg = f"No shop item found for given id ({item_id}). Review and try again."
            log_err(msg)
        except ShopSerializerValidationError as e:
            log_err(f"Error while updating shop item {str(item_id)}. Error : {str(e)}")
            msg = str(e)
        except Exception as e:
            log_err(f"Error while updating shop item. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        msg = ERROR
        try:
            qs = self.get_queryset()
            if kwargs.get("id"):
                instance = qs.get(pk=kwargs.get("id"))
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            qs = self.filter_queryset(qs)
            result_page = self.paginator.paginate_queryset(qs, request)
            serializer = self.get_serializer(result_page, many=True)
            return self.paginator.get_paginated_response(serializer.data)
        except ShopItem.DoesNotExist:
            msg = f"No shop item found for given id ({kwargs.get('id')}). Review and try again."
            log_err(msg)
        except Exception as e:
            log_err(f"Error while getting shop item/s. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        """
        Add items to shop inventory
        """
        msg = ERROR
        data = request.data
        try:
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except ShopSerializerValidationError as e:
            log_err(f"Error while adding shop item {str(data)}. Error : {str(e)}")
            msg = str(e)
        except ValidationError as e:
            log_err(f"Error while adding shop item {str(data)}. Error : {str(e)}")
            msg = str(e.detail)
        except Exception as e:
            log_err(f"Error while adding shop item {str(data)}. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)


class ShopItemRemoveView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        """
        Delete items from shop inventory
        """
        msg = ERROR
        id_list = request.data.get("id")
        try:
            items = ShopItem.objects.filter(pk__in=id_list)
            items.delete()
            return Response({RESPONSE_KEY: DELETED})
        except Exception as e:
            log_err(f"Error while deleting shop items {str(id_list)}. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

