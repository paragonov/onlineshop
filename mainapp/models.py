from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Categories(models.Model):
    name = models.CharField('Название категории', max_length=25, db_index=True, )
    image = models.ImageField('Изображение', upload_to='image/catigories/%Y/%m/%d')
    url = models.SlugField(max_length=52, db_index=True, blank=True, )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, ):
        if not self.id:
            self.url = slugify(self.name)
        super(Categories, self).save(*args)

    def get_absolute_url(self):
        return reverse('scat', kwargs={'cat_slug': self.url})

    def __str__(self):
        return f'{self.name}'


class Brands(models.Model):
    name = models.CharField('Бренд', max_length=40, db_index=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name_model = models.CharField('Название', max_length=100, db_index=True)
    discription = models.TextField('Описание', max_length=1000, db_index=True)
    price = models.IntegerField('Цена', )
    size_discount = models.IntegerField('Скидка', default=0)
    main_image = models.ImageField('Главное изображение', upload_to='image/products/%Y/%m/%d', )
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, )
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, )
    discount = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    url = models.SlugField(max_length=52, db_index=True, blank=True)

    class Meta:
        ordering = ['category']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def price_with_disk(self):
        return self.price - round(self.price * (self.size_discount/100))

    def save(self, *args, ):
        if not self.id:
            self.url = slugify(self.name_model)
        super(Products, self).save(*args)

    def __str__(self):
        return f'{self.name_model}'


class Image(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to=f'image/products/%Y/%m/%d')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.product}'
