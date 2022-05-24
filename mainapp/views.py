from django.shortcuts import render
from django.views.generic import ListView
from .models import Catigories, Products


class MainView(ListView):
    def get(self, request, *args, **kwargs):
        product = Products.objects.order_by('?')[:6]
        catigories = Catigories.objects.order_by('?')[:3]
        context = {
            'prod': product,
            'cat': catigories
        }
        return render(request, 'mainapp/main.html', context=context)