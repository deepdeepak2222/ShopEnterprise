from django.urls import path, re_path

from shop_inventory.views import ShopItemView, ShopItemRemoveView

# from django.urls

urlpatterns = [
    path("", ShopItemView.as_view(), name="Create/List shop item"),
    path("remove/", ShopItemRemoveView.as_view(), name="Remove shop item"),
    re_path("(?P<id>[a-z0-9-]+)/$", ShopItemView.as_view(), name="Get detail of shop item"),
]
