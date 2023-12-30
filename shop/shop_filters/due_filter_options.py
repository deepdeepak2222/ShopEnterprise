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
    return [int(max_min["min"]), int(max_min["max"])]
