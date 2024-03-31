from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.constants import RESPONSE_KEY
from shop_filters.constants import ERRORS
from shop_filters.custom_category_filter_components import get_custom_category_filter_components
from shop_filters.due_filter_components import get_due_filter_components
from shop_filters.shop_items_filter_components import get_shop_items_filter_components
from shop_filters.utils import get_filter_options
from rest_framework.permissions import IsAuthenticated


class ShopFilters(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        module = kwargs.get('module')
        # Map of filter components and their functions
        filter_components = {
            "shop-item": get_shop_items_filter_components,
            "custom-category": get_custom_category_filter_components,
            "due": get_due_filter_components,
        }
        filter_comp_fun = filter_components.get(module)
        if not filter_comp_fun:
            return Response(
                {RESPONSE_KEY: ERRORS.get("INVALID_FILTER_MODULE")},
                status=status.HTTP_400_BAD_REQUEST)
        return Response(filter_comp_fun())


class ShopFilterOptions(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        module = kwargs.get("module")
        key = kwargs.get("key")
        params = {
            "module": module,
            "key": key,
        }
        options = get_filter_options(**params)
        return Response(options)
