from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from core.constants import RESPONSE_KEY
from shop_filters.constants import FILTER_COMPS, ERRORS
from shop_filters.utils import get_filter_options


class ShopFilters(GenericAPIView):
    def get(self, request, *args, **kwargs):
        module = kwargs.get('module')
        filter_comp = FILTER_COMPS.get(module)
        if not filter_comp:
            return Response(
                {RESPONSE_KEY: ERRORS.get("INVALID_FILTER_MODULE")},
                status=status.HTTP_400_BAD_REQUEST)
        return Response(filter_comp)


class ShopFilterOptions(GenericAPIView):
    def get(self, request, *args, **kwargs):
        module = kwargs.get("module")
        key = kwargs.get("key")
        params = {
            "module": module,
            "key": key,
        }
        options = get_filter_options(**params)
        return Response(options)
