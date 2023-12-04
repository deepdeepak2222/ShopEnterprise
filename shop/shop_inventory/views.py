from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.constants import ERROR, RESPONSE_KEY
from core.exceptions import ShopSerializerValidationError
from core.pagination import StandardResultsSetPagination
from log.log import log_err
from shop_inventory.constants import SHOP_ITEM_TSV_SEARCH_Q
from shop_inventory.models import ShopItem
from shop_inventory.serializers import ShopItemSerializer


# Create your views here.


class ShopItemView(GenericAPIView):
    """
    API Type : POST/PUT/LIST/GET
    API: List/Create/Update/GET shop items
    """
    serializer_class = ShopItemSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        if self.request.query_params.get("q"):
            qs = ShopItem.objects.raw(SHOP_ITEM_TSV_SEARCH_Q % self.request.query_params.get("q"))
        else:
            qs = ShopItem.objects.all().order_by("-created")
        return qs

    # def put(self, request, *args, **kwargs):
    #     msg = ERROR
    #     try:
    #         qs = self.get_queryset()
    #         result_page = self.paginator.paginate_queryset(qs, request)
    #         serializer = self.get_serializer(result_page, many=True)
    #         return self.paginator.get_paginated_response(serializer.data)
    #     except Exception as e:
    #         log_err(f"Error while updating/deleting shop item/s. Error : {str(e)}")
    #     return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        msg = ERROR
        try:
            qs = self.get_queryset()
            result_page = self.paginator.paginate_queryset(qs, request)
            serializer = self.get_serializer(result_page, many=True)
            return self.paginator.get_paginated_response(serializer.data)
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
