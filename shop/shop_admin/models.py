from django.db import models

from core.constants import TransactionType
from core.model_utils import TimestampedModel


class Due(TimestampedModel):
    f_name = models.CharField(max_length=50, null=False)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    total_money = models.FloatField(default=0)
    remaining_money = models.FloatField(default=0)
    paid = models.BooleanField(default=False)
    transaction_history = models.ManyToManyField(
        "shop_admin.TransactionDetail", related_name="due_of_transaction"
    )


class TransactionDetail(TimestampedModel):
    """
    Dues detail history
    All the transaction(be it buy more or deposit) will be kept here.
    """
    due = models.ForeignKey(Due, on_delete=models.CASCADE, related_name="due_of_due_history")
    transaction_date = models.DateTimeField()
    total_money = models.FloatField(null=False)
    transaction_detail = models.CharField(max_length=500, null=True, blank=True)
    transaction_type = models.PositiveSmallIntegerField(default=TransactionType.BORROW)
