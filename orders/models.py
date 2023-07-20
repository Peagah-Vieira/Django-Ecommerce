from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


UserModel = get_user_model()


class Order(models.Model):
    PENDING_STATE = "p"
    COMPLETED_STATE = "c"
    ORDER_CHOICES = (
        (PENDING_STATE, "pending"),
        (COMPLETED_STATE, "completed"),
    )

    buyer = models.ForeignKey(
        UserModel,
        related_name='order_buyer',
        on_delete=models.CASCADE,
    )
    order_number = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=1,
        choices=ORDER_CHOICES,
        default=PENDING_STATE,
    )
    is_paid = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='order_items',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name='order_product',
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
