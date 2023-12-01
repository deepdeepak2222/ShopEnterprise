"""
App : Category
Serializer classes.
"""
from rest_framework import serializers
from category.models import CustomCategory


class CustomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCategory
        fields = ("id", "category_type", "name", "description")
        read_only_fields = ("id", "description")

    def create(self, validated_data):
        """
        Create custom category
        """
        validated_data["description"] = self.initial_data.get("description")
        obj = self.Meta.model.objects.create(**validated_data)
        return obj
