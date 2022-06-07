# Generated by Django 4.0.4 on 2022-05-29 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=40, verbose_name='Бренд')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25, verbose_name='Название категории')),
                ('image', models.ImageField(upload_to='image/catigories/%Y/%m/%d', verbose_name='Изображение')),
                ('url', models.SlugField(blank=True, max_length=52)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_model', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('discription', models.TextField(db_index=True, max_length=1000, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('size_discount', models.IntegerField(verbose_name='Цена со скидкой')),
                ('main_image', models.ImageField(upload_to='image/products/%Y/%m/%d', verbose_name='Главное изображение')),
                ('discount', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('url', models.SlugField(blank=True, max_length=52)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.brands')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/products/%Y/%m/%d', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.products')),
            ],
        ),
    ]
