import uuid

from django.db import models

from category.constants import CategoryType


# Create your models here.


class CustomCategory(models.Model):
    CAT_TYPE_CHOICES = (
        (CategoryType.PER_KG, CategoryType.PER_KG),
        (CategoryType.PER_LTR, CategoryType.PER_LTR),
        (CategoryType.PER_PIECE, CategoryType.PER_PIECE),
    )

    id = models.CharField(primary_key=True, default=uuid.uuid4, max_length=36)
    category_type = models.CharField(max_length=15, choices=CAT_TYPE_CHOICES)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        unique_together = (
            ("category_type", "name")
        )


