# Generated by Django 4.0.4 on 2022-05-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='size_discount',
            field=models.IntegerField(default=0, verbose_name='Скидка'),
        ),
    ]
