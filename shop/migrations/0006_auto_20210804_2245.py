# Generated by Django 3.2.5 on 2021-08-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_course_lvl_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apparel',
            name='size',
        ),
        migrations.AddField(
            model_name='apparel',
            name='sizes',
            field=models.ManyToManyField(related_name='apparel_size', through='shop.ApparelSize', to='shop.Size'),
        ),
    ]
