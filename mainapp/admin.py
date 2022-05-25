from django.contrib import admin

from mainapp.models import Products, Categories, Image


class CatAdmin(admin.ModelAdmin):
    fields = ('name', 'url', 'image')
    prepopulated_fields = {"url": ("name",)}

    class Meta:
        model = Categories


class ProductsAdmin(admin.ModelAdmin):
    fields = ('name_model', 'price', 'available', 'url', 'brand', 'category', 'main_image')
    list_display = ('category', 'name_model', 'price', 'available')
    prepopulated_fields = {'url': ('name_model',)}
    ordering = ('category',)
    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories, CatAdmin)
admin.site.register(Image)
