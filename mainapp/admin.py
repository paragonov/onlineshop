from django.contrib import admin

from mainapp.models import Products, Categories, Image, Brands


class CatAdmin(admin.ModelAdmin):
    fields = ("name", "url", "image")
    prepopulated_fields = {"url": ("name",)}

    class Meta:
        model = Categories


class ProductsAdmin(admin.ModelAdmin):
    fields = (
        "category",
        "brand",
        "name_model",
        "main_image",
        "available",
        "discount",
        "size_discount",
        "url",
        "price",
    )
    list_display = ("category", "brand", "name_model", "price", "available")
    prepopulated_fields = {"url": ("name_model",)}
    ordering = ("category",)

    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories, CatAdmin)
admin.site.register(Image)
admin.site.register(Brands)
