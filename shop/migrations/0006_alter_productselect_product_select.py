# Generated by Django 3.2.5 on 2021-08-17 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210817_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productselect',
            name='product_select',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_selected', to='shop.productoption'),
        ),
    ]
