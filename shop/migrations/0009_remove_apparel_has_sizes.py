# Generated by Django 3.2.5 on 2021-08-06 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210804_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apparel',
            name='has_sizes',
        ),
    ]
