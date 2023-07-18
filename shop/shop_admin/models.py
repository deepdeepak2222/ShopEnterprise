from django.db import models
from django.db.models import JSONField

from core.model_utils import TimestampedModel


class Due(TimestampedModel):
    f_name = models.CharField(max_length=50, null=False)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    total_money = models.FloatField(null=False)
    payment_history = JSONField(default=dict)
    remaining_money = models.FloatField(null=False)
