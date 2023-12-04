from django.urls import path

from shop_inventory.views import ShopItemView

# from django.urls

urlpatterns = [
    path("", ShopItemView.as_view()),
]
