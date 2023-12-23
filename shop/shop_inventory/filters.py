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

    class Meta:
        model = ShopItem
        fields = ()

