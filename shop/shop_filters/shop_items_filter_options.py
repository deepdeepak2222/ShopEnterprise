"""
Filter option functions for shop items
"""
from django.db.models import Max, Min

from category.constants import CategoryType
from category.models import CustomCategory
from shop_inventory.models import ShopItem


def get_shop_items_categories(**kwargs):
    """
    Get categories
    """
    qs = CustomCategory.objects.all().order_by("name")
    return [{
        "label": cat.name,
        "value": cat.id,
    } for cat in qs]


def get_shop_items_category_types(**kwargs):
    """
    Get category types
    """
    return [{
        "label": i.get("label"),
        "value": i.get("id"),
    } for i in CategoryType.CAT_LABELS]


def get_shop_item_total_range():
    """
    Get shop item's total property's range (so far in db)
    """
    max_min = ShopItem.objects.aggregate(max=Max('total'), min=Min('total'))
    min_item = int(max_min.get("min", 0)) if max_min.get("min", 0) else 0
    max_item = int(max_min.get("max", 0)) if max_min.get("max", 0) else 0
    return [min_item, max_item]


def get_shop_item_price_range():
    """
    Get shop item's price property's range (so far in db)
    """
    max_min = ShopItem.objects.aggregate(max=Max('price'), min=Min('price'))
    min_item = int(max_min.get("min", 0)) if max_min.get("min", 0) else 0
    max_item = int(max_min.get("max", 0)) if max_min.get("max", 0) else 0
    return [min_item, max_item]
