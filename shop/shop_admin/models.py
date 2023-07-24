from django.db import models

from core.model_utils import TimestampedModel


class Due(TimestampedModel):
    f_name = models.CharField(max_length=50, null=False)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    total_money = models.FloatField(default=0)
    payment_history = models.ManyToManyField("shop_admin.DuePayment", related_name="due_payment_history")
    remaining_money = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    due_history = models.ManyToManyField("shop_admin.DueDetail", related_name="due_history")


class DuePayment(TimestampedModel):
    """
    Dues payment history
    """
    due = models.ForeignKey(Due, on_delete=models.CASCADE, related_name="due_of_payment")
    pay_date = models.DateTimeField()
    total_money = models.FloatField(null=False)
    payment_detail = models.CharField(max_length=500, null=True, blank=True)


class DueDetail(TimestampedModel):
    """
    Dues detail history
    """
    due = models.ForeignKey(Due, on_delete=models.CASCADE, related_name="due_of_due_history")
    due_date = models.DateTimeField()
    total_money = models.FloatField(null=False)
    due_detail = models.CharField(max_length=500, null=True, blank=True)
