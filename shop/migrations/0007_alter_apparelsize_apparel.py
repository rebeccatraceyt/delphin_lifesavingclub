# Generated by Django 3.2.5 on 2021-08-04 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210804_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparelsize',
            name='apparel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apparel_sizes', to='shop.apparel'),
        ),
    ]
