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
