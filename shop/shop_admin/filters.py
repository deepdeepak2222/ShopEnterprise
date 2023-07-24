"""
Filter classes
"""
from shop_admin.models import Due
import django_filters
from django_filters import rest_framework as filters


class DueFilter(django_filters.FilterSet):
    """
    Filter class for Due model.
    """
    total_money__exact = filters.NumberFilter(
        field_name="total_money", lookup_expr="exact"
    )
    total_money__lte = filters.NumberFilter(
        field_name="total_money", lookup_expr="lte"
    )
    total_money__gte = filters.NumberFilter(
        field_name="total_money", lookup_expr="gte"
    )
    phone__contains = filters.CharFilter(field_name="phone", lookup_expr="contains")

    class Meta:
        model = Due
        fields = (
            "total_money__exact",
            "total_money__lte",
            "total_money__gte",
            "phone__contains",
        )
