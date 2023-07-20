from rest_framework import serializers
from accounts.serializers import AccountsSerializer
from products.serializers import ProductSerializer
from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'buyer',
            'buyer_details',
            'order_number',
            'status',
            'is_paid',
            'created_at',
            'updated_at',
        ]

    buyer_details = AccountsSerializer(
        source='buyer',
        read_only=True,
    )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'order',
            'order_details',
            'product',
            'product_details',
            'quantity',
            'total',
            'created_at',
            'updated_at',
        ]

    order_details = OrderSerializer(
        source='order',
        read_only=True,
    )

    product_details = ProductSerializer(
        source='product',
        read_only=True,
    )
