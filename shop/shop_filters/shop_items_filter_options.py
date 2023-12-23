"""
Filter option functions for shop items
"""
from category.constants import CategoryType
from category.models import CustomCategory


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
