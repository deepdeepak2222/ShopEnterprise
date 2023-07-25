"""
Serializer classes for shop admin module
"""
from rest_framework import serializers

from core.utils import date_time_from_timestamp
from shop_admin.models import Due, DueDetail, DuePayment


class PaymentHistorySerializer(serializers.ModelSerializer):
    """
    Payment history serializer
    """
    pay_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DuePayment
        fields = (
            "id",
            "due",
            "pay_date",
            "total_money",
            "payment_detail",
        )

    @staticmethod
    def get_pay_date(obj):
        """
        Get pay date
        """
        return int(obj.pay_date.timestamp())


class DueHistorySerializer(serializers.ModelSerializer):
    """
    Due history serializer
    """
    due_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DueDetail
        fields = (
            "id",
            "due",
            "due_date",
            "total_money",
            "due_detail",
        )

    @staticmethod
    def get_due_date(obj):
        """
        Get due date
        """
        return int(obj.due_date.timestamp())


class DueDetailSerializer(serializers.ModelSerializer):
    due_history = DueHistorySerializer(read_only=True, many=True)
    payment_history = PaymentHistorySerializer(read_only=True, many=True)

    class Meta:
        model = Due
        fields = (
            "id", "f_name", "l_name", "phone", "total_money",
            "remaining_money", "payment_history", "paid", "due_history"
        )
        read_only_fields = (
            "remaining_money", "payment_history",
            "id", "paid", "total_money",
            "due_history"
        )

    def validate(self, attrs):
        if not self.initial_data.get("due_detail"):
            raise serializers.ValidationError({"due_detail": "Due detail is not provided."})
        return attrs

    def create(self, validated_data):
        """
        Create due
        """
        due = Due.objects.create(**validated_data)
        # Update payment history
        try:
            self.update_due_history(due, self.initial_data.get("due_detail"))
        except serializers.ValidationError as e:
            Due.objects.filter(pk=due.pk).delete()
            raise e
        return due

    @staticmethod
    def update_due_history(due, due_detail):
        """
        Update due history
        """
        # update due detail
        due_fields = ("due_date", "due_detail", "total_money")
        for field in due_fields:
            if field not in due_detail:
                raise serializers.ValidationError({field: "%s not present in due_detail object" % field})
        DueDetailSerializer.create_due_history(due, due_detail)

    @staticmethod
    def create_due_history(due, due_detail):
        """
        Create due history
        """
        history = {
            "due": due,
            "due_date": date_time_from_timestamp(due_detail.get("due_date")),
            "total_money": due_detail.get("total_money"),
            "due_detail": due_detail.get("due_detail"),
        }
        due_history_obj = DueDetail.objects.create(**history)
        due.total_money = due.total_money + history.get("total_money")
        due.save(update_fields=["total_money"])
        due.due_history.add(due_history_obj)


class DueListSerializer(DueDetailSerializer):
    class Meta:
        model = Due
        fields = ("id", "f_name", "l_name", "phone", "total_money", "remaining_money")
        read_only_fields = ("remaining_money", "payment_history", "id")
