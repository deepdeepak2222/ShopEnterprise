import uuid

from django.db import models

from category.constants import CategoryType
from category.models import CustomCategory
from core.model_utils import TimestampedModel


class ShopItem(TimestampedModel):
    """
    Item and its details
    """
    CAT_TYPE_CHOICES = (
        (CategoryType.PER_KG, CategoryType.PER_KG),
        (CategoryType.PER_LTR, CategoryType.PER_LTR),
        (CategoryType.PER_PIECE, CategoryType.PER_PIECE),
    )

    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36)
    barcode = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    total = models.FloatField(default=0)
    category = models.ForeignKey(
        CustomCategory, on_delete=models.SET_NULL,
        related_name="cust_category_items", null=True
    )
    category_type = models.CharField(max_length=15, choices=CAT_TYPE_CHOICES)
    price = models.FloatField()
