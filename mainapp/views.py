from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Categories, Products


class MainView(View):
    def get(self, request, *args, **kwargs):
        prod = Products.objects.order_by('?')[:6]
        categories = Categories.objects.order_by('?')[:3]
        context = {
            'prod': prod,
            'cat': categories,
        }
        return render(request, 'mainapp/main.html', context=context)


class ProductsView(View):
    def get(self, request, *args, **kwargs ):
        prod = Products.objects.all()
        brands = Products.objects.values('brand').distinct()
        cats = Categories.objects.all()
        context = {
            'prod':prod,
            "brands": brands,
            'cats': cats
        }
        return render(request, 'mainapp/categories.html', context=context)


class SelectCatView(View):
    def get(self, request, *args, **kwargs):
        brands = Products.objects.values('brand').distinct()
        cats = Categories.objects.all()
        filter_brand = request.GET.getlist('brand')
        filter_cats = request.GET.getlist('cat')
        result_set = []
        if not filter_brand and not filter_cats:
            prod = Products.objects.all()
            return render(request, 'mainapp/select_category.html', context={
                'prod': prod,
                "brands": brands,
                'cats': cats
            })
        if filter_brand and filter_cats:
            for c in filter_cats:
                for b in filter_brand:
                    result_set.extend(Products.objects.filter(Q(brand__icontains=b) & Q(category__name__icontains=c)))
        elif filter_brand or filter_cats:
            for c in filter_cats:
                obj_cat = Products.objects.filter(Q(category__name__icontains=c))
                result_set.extend(obj_cat)
            for b in filter_brand:
                obj_brand = Products.objects.filter(Q(brand__icontains=b))
                result_set.extend(obj_brand)
        return render(request, 'mainapp/select_category.html', context={
            'prod': set(result_set),
            "brands": brands,
            'cats': cats
        })
