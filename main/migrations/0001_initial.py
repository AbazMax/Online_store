# Generated by Django 4.1.2 on 2022-10-25 09:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('month', 'month'), ('week', 'week'), ('day', 'day')], max_length=50)),
                ('title', models.CharField(db_index=True, max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('sale_value', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(99)])),
                ('end_of_promo', models.DateTimeField()),
                ('position', models.PositiveSmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Promo',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('position', models.SmallIntegerField()),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to=main.models.Product.get_file_name)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unit', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('position',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]