from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    image = models.ImageField(upload_to='items_images/%Y/%m/%d/', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=False, verbose_name='Готово к отправке')
    current_location = models.CharField(max_length=255, verbose_name='Текущее местоположение')
    expected_location = models.CharField(max_length=255, verbose_name='Местоположение прибытия')

    def __str__(self):
        return self.name
