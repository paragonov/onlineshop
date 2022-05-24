from django.contrib import admin

from mainapp.models import Products, Catigories, Image


class CatAdmin(admin.ModelAdmin):
    fields = ('name', 'url', 'image')
    prepopulated_fields = {"url": ("name",)}

    class Meta:
        model = Catigories


class ProductsAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'available', 'url', 'category', 'main_image')
    list_display = ('category', 'name', 'price', 'available')
    prepopulated_fields = {'url': ('name',)}
    ordering = ('category',)
    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)
admin.site.register(Catigories, CatAdmin)
admin.site.register(Image)
