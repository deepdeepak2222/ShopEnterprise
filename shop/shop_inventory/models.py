from django.db import models

from core.model_utils import TimestampedModel
from shop_inventory.enums import PriceType


class ShopItemCategory(TimestampedModel):
    """
    Item category. Example: Biscuit, Grocery, Cosmetic, Liquid Food etc
    """
    label = models.CharField(max_length=100, unique=True)


# Create your models here.

class ShopItem(TimestampedModel):
    """
    Item and its details
    """
    PRICE_TYPE_CHOICES = (
        (PriceType.L, PriceType.L),
        (PriceType.KG, PriceType.KG),
        (PriceType.QUANT, PriceType.QUANT),
    )
    barcode = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)
    category = models.ForeignKey(
        ShopItemCategory, on_delete=models.SET_NULL,
        related_name="category_items", null=True
    )
    price_type = models.CharField(
        max_length=10, choices=PRICE_TYPE_CHOICES,
        default=PriceType.QUANT
    )
    price = models.FloatField()
