# Generated by Django 4.2.7 on 2023-11-25 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_inventoryitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='items_images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='category',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.PROTECT, to='inventory.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='current_location',
            field=models.CharField(default='xx', max_length=255, verbose_name='Текущее местоположение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='expected_location',
            field=models.CharField(default='xxx', max_length=255, verbose_name='Местоположение прибытия'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='is_available',
            field=models.BooleanField(default=False, verbose_name='Готово к отправке'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]