from django.urls import path

from rest_auth.views import LoginView


urlpatterns = [
    path("login/", LoginView.as_view()),
]
