"""
Utilities for shop app
"""
from datetime import datetime


def date_time_from_timestamp(timestamp):
    """
    Get Datetime object from timestamp
    """
    dt_object = datetime.fromtimestamp(int(timestamp//1000))
    return dt_object


def get_sort_key(sort, default_sort, sort_keys):
    """
    Get sort key from request query param
    """
    sort_tmp = sort
    if sort_tmp.startswith("-"):
        sort_tmp = sort_tmp[1:]
    if sort_tmp not in sort_keys:
        sort = default_sort
    return sort
