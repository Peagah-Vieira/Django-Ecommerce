from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'category',
            'price',
            'created_at',
            'updated_at',
        ]
