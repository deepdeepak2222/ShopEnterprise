from django_filters import rest_framework as filters
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from core.constants import RESPONSE_KEY, ERROR
from core.pagination import StandardResultsSetPagination
from core.utils import get_sort_key
from shop_admin.filters import DueFilter
from shop_admin.models import Due
from shop_admin.serializers import DueDetailSerializer, DueListSerializer
from shop_admin.utils import make_due_payment


# Create your views here.

class DueView(ListAPIView, CreateAPIView, UpdateAPIView):
    model_class = Due
    filterset_class = DueFilter
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    sort_keys = ("modified", "created", "f_name", "l_name", "phone", "total_money")
    default_sort = "-modified"

    def get_queryset(self):
        sort = self.request.query_params.get("sort", "-modified")
        sort = get_sort_key(sort, self.default_sort, self.sort_keys)
        return Due.objects.all().order_by(sort)

    def get_serializer_class(self):
        if self.request.query_params.get("id") or self.request.method in ("POST", "PUT"):
            return DueDetailSerializer
        return DueListSerializer

    def get(self, request, *args, **kwargs):
        msg = ERROR
        try:
            due_id = request.query_params.get("id")
            if due_id:
                due = Due.objects.get(pk=due_id)
                serializer = DueDetailSerializer(due)
                return Response(serializer.data)
            qs = self.get_queryset()
            qs = self.filter_queryset(qs)
            # get paginated response
            result_page = self.paginator.paginate_queryset(qs, request)
            serializer = DueListSerializer(result_page, many=True)
            return self.paginator.get_paginated_response(serializer.data)
        except Due.DoesNotExist:
            msg = "Due does not exist for id: %s" % due_id
        except Exception as e:
            print(str(e))
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Update due
        """
        data = request.data
        msg = ERROR
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


class DuePaymentView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        msg = ERROR
        due_id = None
        try:
            data = request.data
            due_id = data.get("id")
            due = Due.objects.get(pk=due_id)
            payment_detail = data.get("payment_detail")
            make_due_payment(due, payment_detail)
            serializer = DueDetailSerializer(due)
            return Response(serializer.data)
        except Due.DoesNotExist:
            msg = "Due does not exist for given id : %s" % due_id
        except serializers.ValidationError as e:
            print(str(e))
            msg = e.detail
        except Exception as e:
            print(str(e))
        return Response({RESPONSE_KEY: msg}, status=status.HTTP_400_BAD_REQUEST)
