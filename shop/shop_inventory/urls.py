from django.urls import path, re_path

from shop_inventory.views import ShopItemView, ShopItemRemoveView

# from django.urls

urlpatterns = [
    path("", ShopItemView.as_view()),
    re_path(r"(?P<id>[a-z0-9-]+)/$", ShopItemView.as_view()),
    path("remove/", ShopItemRemoveView.as_view()),
]
