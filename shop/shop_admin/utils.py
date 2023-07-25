"""
Utilities for shop admin module
"""
from rest_framework import serializers

from core.utils import date_time_from_timestamp
from shop_admin.models import DuePayment


def make_due_payment(due, payment_detail):
    """
    "payment_detail": {
            "payment_date": 1690172976,
            "payment_detail": "Bought a pen",
            "total_money": 10
        }
    """
    if not isinstance(payment_detail, dict):
        raise serializers.ValidationError({"payment_detail": "Invalid payment_detail. It must be an object."})
    payment_detail_mandatory_fields = ("payment_date", "total_money")
    for field in payment_detail_mandatory_fields:
        if field not in payment_detail:
            raise serializers.ValidationError({"payment_detail": "%s not present in payment_detail." % field})
    if due.total_money < payment_detail.get("total_money"):
        raise serializers.ValidationError({"payment_detail": "Excessive payment."})
    payment_data = {
        "due": due,
        "pay_date": date_time_from_timestamp(payment_detail.get("payment_date")),
        "total_money": payment_detail.get("total_money"),
        "payment_detail": payment_detail.get("payment_detail"),
    }
    payment = DuePayment.objects.create(**payment_data)
    due.payment_history.add(payment)
    due.total_money = due.total_money - payment_detail.get("total_money")
    due.save()
