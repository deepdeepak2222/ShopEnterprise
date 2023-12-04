"""
App : Shop Items
Serializer classes.
"""
from rest_framework import serializers

from category.models import CustomCategory
from category.serializers import CustomCategorySerializer
from core.exceptions import ShopSerializerValidationError
from shop_inventory.models import ShopItem


class ShopItemSerializer(serializers.ModelSerializer):
    category = CustomCategorySerializer(read_only=True)

    class Meta:
        model = ShopItem
        fields = ("id", "barcode", "name", "description", "total", "category", "category_type", "price")
        read_only_fields = ("id", "description", "total", "category",)

    def validate(self, attrs):
        """
        Validate data
        """
        category = self.initial_data.get("category")
        if isinstance(category, dict):
            try:
                category = CustomCategory.objects.get(pk=category.get("id"))
                attrs["category_type"] = category.category_type
                attrs["category"] = category
            except CustomCategory.DoesNotExist:
                raise ShopSerializerValidationError(
                    f"Category does not exists for the given id {category}. Review and try again.")
        attrs["total"] = self.initial_data.get("total")
        attrs["description"] = self.initial_data.get("description")
        return attrs

    def create(self, validated_data):
        return ShopItem.objects.create(**validated_data)

