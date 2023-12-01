"""
Filter classes
"""
import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters

from category.models import CustomCategory


class CustomCategoryFilter(django_filters.FilterSet):
    """
    Filter class for CustomCategory model.
    """
    q = filters.CharFilter(method="search_custom_category")

    class Meta:
        model = CustomCategory
        fields = ()

    @staticmethod
    def search_custom_category(qs, name, value):
        print(f"qs:{qs}, name: {name}, value: {value}")
        fil_exp = Q(name__icontains=value) | \
                  Q(category_type__icontains=value) | \
                  Q(description__icontains=value)
        return qs.filter(fil_exp)
