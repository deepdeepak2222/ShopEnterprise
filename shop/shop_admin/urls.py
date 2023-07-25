from django.urls import path

from shop_admin.views import DueView, DuePaymentView

# from django.urls

urlpatterns = [
    path("due/", DueView.as_view()),
    path("due/payment/", DuePaymentView.as_view()),
]
