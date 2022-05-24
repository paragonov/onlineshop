from django.db import models
from django.utils.text import slugify


class Catigories(models.Model):
    name = models.CharField('Название категории', max_length=25, db_index=True, )
    image = models.ImageField('Изображение', upload_to='image/catigories/%Y/%m/%d')
    url = models.SlugField(max_length=52, db_index=True, blank=True, )

    def save(self, *args, ):
        if not self.id:
            self.url = slugify(self.name)
        super(Catigories, self).save(*args)

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name = models.CharField('Название', max_length=100, db_index=True)
    discription = models.TextField('Описание', max_length=1000, db_index=True)
    price = models.IntegerField('Цена', )
    main_image = models.ImageField('Главное изображение', upload_to='image/products/%Y/%m/%d',)
    category = models.ForeignKey(Catigories, on_delete=models.CASCADE, )
    url = models.SlugField(max_length=52, db_index=True, blank=True)
    available = models.BooleanField(default=True)

    def save(self, *args, ):
        if not self.id:
            self.url = slugify(self.name)
        super(Products, self).save(*args)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to=f'image/products/%Y/%m/%d')

    def __str__(self):
        return f'{self.product}'
