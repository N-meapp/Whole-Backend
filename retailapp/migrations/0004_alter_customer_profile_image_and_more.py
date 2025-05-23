# Generated by Django 5.1.5 on 2025-04-07 10:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailapp', '0003_alter_administrator_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='http://res.cloudinary.com/djedeaw0l/image/upload/v1/customerprofile/w7kmmmmsibzmn5lfu1qx', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_description',
            field=models.TextField(),
        ),
    ]
