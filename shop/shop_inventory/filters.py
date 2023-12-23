"""
Filter classes
"""
import django_filters
from django_filters import rest_framework as filters

from shop_inventory.models import ShopItem


class ShopItemFilter(django_filters.FilterSet):
    """
    Filter class for ShopItem model.
    """
    category = filters.CharFilter(field_name="category_id", lookup_expr="exact")
    category_type = filters.CharFilter(field_name="category_type", lookup_expr="exact")
    total_from = filters.NumberFilter(field_name="total", lookup_expr="gte")
    total_to = filters.NumberFilter(field_name="total", lookup_expr="lte")
    price_from = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_to = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = ShopItem
        fields = ()

