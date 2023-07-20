from rest_framework import serializers
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'buyer',
            'order_number',
            'status',
            'is_paid',
            'created_at',
            'updated_at',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'order',
            'product',
            'quantity',
            'total',
            'created_at',
            'updated_at',
        ]
