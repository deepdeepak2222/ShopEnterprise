from django.urls import re_path

from shop_filters.views import ShopFilters, ShopFilterOptions

urlpatterns = [
    re_path("(?P<module>[a-z-]+)/$", ShopFilters.as_view(), name="Get filter components for a module"),
    re_path("(?P<module>[a-z-]+)/(?P<key>[a-z-]+)/$",
            ShopFilterOptions.as_view(), name="Get filter options for a filter component"),
]
