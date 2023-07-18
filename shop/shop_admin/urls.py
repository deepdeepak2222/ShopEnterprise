from django.urls import path

from shop_admin.views import DueView

# from django.urls

urlpatterns = [
    path("due/", DueView.as_view())
]
