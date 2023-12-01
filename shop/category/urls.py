from django.urls import path

from category.views import CategoryTypeView, CustomCategoryView

# from django.urls

urlpatterns = [
    path("", CategoryTypeView.as_view()),
    path("custom-category/", CustomCategoryView.as_view()),
]
