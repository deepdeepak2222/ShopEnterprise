"""
Custom Error classes
"""

from rest_framework.exceptions import ValidationError


class ShopSerializerValidationError(ValidationError):
    """
    Raise all the serializer validation
    """
    pass
