# Generated by Django 4.2.7 on 2023-11-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_inventoryitem_image_alter_inventoryitem_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='image',
            field=models.ImageField(upload_to='items_images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
