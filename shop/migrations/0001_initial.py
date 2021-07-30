# Generated by Django 3.2.5 on 2021-07-28 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Apparel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('age_range', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.agerange')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CourseTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_count', models.IntegerField(default=12)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.course')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.time')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.producttype'),
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.ManyToManyField(through='shop.CourseTime', to='shop.Time'),
        ),
        migrations.CreateModel(
            name='ApparelSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_count', models.IntegerField(default=12)),
                ('apparel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.apparel')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.size')),
            ],
        ),
        migrations.AddField(
            model_name='apparel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category'),
        ),
        migrations.AddField(
            model_name='apparel',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.producttype'),
        ),
        migrations.AddField(
            model_name='apparel',
            name='size',
            field=models.ManyToManyField(through='shop.ApparelSize', to='shop.Size'),
        ),
    ]