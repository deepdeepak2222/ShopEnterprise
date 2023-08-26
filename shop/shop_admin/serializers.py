"""
Serializer classes for shop admin module
"""
from rest_framework import serializers

from core.constants import TransactionType
from core.utils import date_time_from_timestamp
from shop_admin.models import Due, TransactionDetail


class DueDetailSerializer(serializers.ModelSerializer):
    transaction_history = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Due
        fields = (
            "id", "f_name", "l_name", "phone", "total_money",
            "remaining_money", "paid",
            "full_name", "transaction_history"
        )
        read_only_fields = (
            "remaining_money", "id", "paid",
            "total_money", "full_name", "transaction_history"
        )

    @staticmethod
    def get_full_name(obj):
        return "%s %s" % (obj.f_name, obj.l_name)

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
            "transaction_date": date_time_from_timestamp(due_detail.get("due_date")),
            "total_money": due_detail.get("total_money"),
            "transaction_detail": due_detail.get("due_detail"),
            "transaction_type": TransactionType.BORROW,
        }
        due_history_obj = TransactionDetail.objects.create(**history)
        due.total_money = due.total_money + history.get("total_money")
        due.save(update_fields=["total_money"])
        due.transaction_history.add(due_history_obj)

    @staticmethod
    def get_transaction_history(obj):
        """
        Get transaction history
        """
        transactions = TransactionDetail.objects.filter(due=obj).order_by("-transaction_date")
        transactions_history = []
        for trans in transactions:
            transactions_history.append(
                {
                    "transaction_date": int(trans.transaction_date.timestamp()*1000),
                    "total_money": trans.total_money,
                    "transaction_detail": trans.transaction_detail,
                    "transaction_type": trans.transaction_type,
                }
            )
        return transactions_history


class DueListSerializer(DueDetailSerializer):
    class Meta:
        model = Due
        fields = ("id", "phone", "total_money", "remaining_money", "full_name")
        read_only_fields = ("remaining_money", "id", "full_name")
