# Generated by Django 3.2.5 on 2021-07-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210728_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lvl_age',
            field=models.CharField(default=0, max_length=254),
        ),
    ]
