# Generated by Django 3.2.5 on 2021-08-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_productselect_product_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='course_info',
            field=models.TextField(default='test'),
        ),
    ]
