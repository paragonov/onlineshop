import datetime

from django.db import models

from mainapp.models import Products


class Reviews(models.Model):
    name = models.CharField('Имя клиента', max_length=55, db_index=True)
    email = models.EmailField('Email, клиента', db_index=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Название продукта')
    rating = models.IntegerField('Оценка',)
    comment = models.TextField('Комментарий', max_length=255, db_index=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзывы'


