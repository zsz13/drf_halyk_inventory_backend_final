from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    current_location = models.CharField(max_length=255, null=True)
    expected_location = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
