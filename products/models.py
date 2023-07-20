from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True,
    )
    description = models.TextField(
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


class Product(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField(
        max_length=100,
    )
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
