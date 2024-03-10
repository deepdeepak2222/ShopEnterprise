"""
Filter option functions for due/borrower module
"""
from django.db.models import Max, Min

from shop_admin.models import Due


def get_total_due_range():
    """
    Get total individual due's range(maximum and minimum borrowed amount)
    """
    max_min = Due.objects.aggregate(max=Max('total_money'), min=Min('total_money'))
    min_item = int(max_min.get("min", 0)) if max_min.get("min", 0) else 0
    max_item = int(max_min.get("max", 0)) if max_min.get("max", 0) else 0
    return [min_item, max_item]
