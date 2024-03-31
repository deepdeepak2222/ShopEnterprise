from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from django_filters import rest_framework as filters

from category.constants import CategoryType
from category.filters import CustomCategoryFilter
from category.models import CustomCategory
from category.serializers import CustomCategorySerializer
from core.constants import RESPONSE_KEY, ERROR, DELETED
from log.log import log_info, log_err
from rest_framework.permissions import IsAuthenticated


class CategoryTypeView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    """
    List basic category types
    """

    def get(self, request, *args, **kwargs):
        return Response(CategoryType.CAT_LABELS)


class CustomCategoryView(GenericAPIView):
    """
    API to CREATE/UPDATE/LIST/GET custom sub categories
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomCategorySerializer
    filterset_class = CustomCategoryFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        return CustomCategory.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        msg = ERROR
        try:
            log_info(f"Creating custom category {str(data)}")
            serializer = self.get_serializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except ValidationError as e:
            msg = str(e.detail[list(e.detail.keys())[0]])
        except Exception as e:
            log_err(f"Error while creating custom category {str(data)}. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        msg = ERROR
        try:
            log_info(f"Listing custom category")
            qs = self.get_queryset()
            qs = self.filter_queryset(qs)
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data)
        except Exception as e:
            log_err(f"Error while fetching custom category. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Delete a custom category
        """
        data = request.data
        msg = ERROR
        try:
            log_info(f"Deleting custom category {str(data)}")
            cust_cat = CustomCategory.objects.filter(pk__in=data.get("id"))
            if not cust_cat.exists():
                msg = f"Invalid category ids({data.get('id')}). No categories found to delete. Please review and try " \
                      f"again. "
                return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)
            cust_cat.delete()
            return Response({RESPONSE_KEY: DELETED})
        except ValidationError as e:
            msg = str(e.detail[list(e.detail.keys())[0]])
        except Exception as e:
            log_err(f"Error while deleting custom category {str(data)}. Error : {str(e)}")
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)
