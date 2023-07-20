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

    category = CategorySerializer()

    def create(self, validated_data):
        categories_data = validated_data.pop("category")
        category = Category.objects.create(**categories_data)
        product = Product.objects.create(category=category, **validated_data)
        return product

    def update(self, instance, validated_data):
        if 'category' in validated_data:
            nested_serializer = self.fields['category']
            nested_instance = instance.category
            nested_data = validated_data.pop('category')

            nested_serializer.update(nested_instance, nested_data)

        return super(ProductSerializer, self).update(instance, validated_data)
