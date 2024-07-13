from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from core.constants import ERROR, RESPONSE_KEY
from log.log import log_err
from rest_auth.models import TokenModel
from rest_auth.serializers import UserLoginSerializer  # Replace with your user serializer


class LoginView(APIView):
    """
    Login view
    """
    def post(self, request, *args, **kwargs):
        try:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token, _ = TokenModel.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            log_err(str(e))
            msg = e.detail
            code = e.status_code
        except Exception as e:
            log_err(str(e))
            msg = ERROR
            code = status.HTTP_400_BAD_REQUEST
        return Response({RESPONSE_KEY: msg}, status=code)
