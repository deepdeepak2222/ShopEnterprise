"""
Model utilities
Created : 8 June 2023
Creator: Deep
"""

from django.db import models


class TimestampedModel(models.Model):
    """
    Timestamp Model class.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
