from django_filters import rest_framework as filters
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from core.constants import RESPONSE_KEY
from shop_admin.filters import DueFilter
from shop_admin.models import Due
from shop_admin.serializers import DueDetailSerializer, DueListSerializer


# Create your views here.

class DueView(ListAPIView, CreateAPIView, UpdateAPIView):
    model_class = Due
    filterset_class = DueFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        print("Came here")
        return Due.objects.all()

    def get_serializer_class(self):
        if self.request.query_params.get("id") or self.request.method in ("POST", "PUT"):
            return DueDetailSerializer
        return DueListSerializer

    def put(self, request, *args, **kwargs):
        """
        Update due
        """
        data = request.data
        msg = "Error Occurred"
        try:
            if not data.get("due_detail"):
                raise serializers.ValidationError({"due_detail": "Due detail is not provided."})
            due_id = data.get("id")
            due = Due.objects.get(pk=due_id)
            DueDetailSerializer.update_due_history(due, data.get("due_detail"))
            r_data = DueDetailSerializer(due).data
            return Response(r_data)
        except Due.DoesNotExist:
            msg = "Due does not exist for id(%s)" % due_id
            print(msg)
        except serializers.ValidationError as e:
            msg = e.detail
            print(msg)
        except Exception as e:
            print("Error occurred while updating the due(%s): %s" % (data.get("id"), str(e)))
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)
