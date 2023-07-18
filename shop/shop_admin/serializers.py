"""
Serializer classes for shop admin module
"""
from rest_framework import serializers

from shop_admin.models import Due


class DueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Due
        fields = ("f_name", "l_name", "phone", "total_money", "remaining_money", "payment_history")
        read_only_fields = ("remaining_money", "payment_history")

    def validate(self, attrs):
        if not self.instance:
            attrs["remaining_money"] = attrs["total_money"]
        return attrs


class DueListSerializer(DueDetailSerializer):
    class Meta:
        model = Due
        fields = ("f_name", "l_name", "phone", "total_money", "remaining_money")
        read_only_fields = ("remaining_money", "payment_history")
