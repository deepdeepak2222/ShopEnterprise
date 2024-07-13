from rest_framework import serializers
from rest_framework import status

from rest_auth.constants import USR_NOT_FOUND
from rest_auth.models import AdminUser  # Replace with your user model


class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = AdminUser
        fields = ("username", "password")  # Adjust fields as needed

    def validate(self, attrs):
        username = self.initial_data.get("username")
        password = self.initial_data.get("password")
        user = AdminUser.objects.filter(username=username, password=password).first()
        if not user:
            raise serializers.ValidationError(detail=USR_NOT_FOUND, code=status.HTTP_400_BAD_REQUEST)
        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        return validated_data["user"]

    def update(self, instance, validated_data):
        return validated_data["user"]


