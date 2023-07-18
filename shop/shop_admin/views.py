from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView

from shop_admin.filters import DueFilter
from shop_admin.models import Due
from shop_admin.serializers import DueDetailSerializer, DueListSerializer
from django_filters import rest_framework as filters


# Create your views here.

class DueView(ListAPIView, CreateAPIView):
    model_class = Due
    filterset_class = DueFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        print("Came here")
        return Due.objects.all()

    def get_serializer_class(self):
        if self.request.query_params.get("id"):
            return DueDetailSerializer
        return DueListSerializer
