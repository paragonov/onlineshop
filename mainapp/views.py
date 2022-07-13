from django.shortcuts import render, get_object_or_404
from django.views import View

from cartapp.cart import Cart
from cartapp.forms import CartAddProductForm
from .models import Categories, Products


class MainView(View):

    def get(self, request, *args, **kwargs):
        prod = Products.objects.order_by('?')[:6]
        categories = Categories.objects.order_by('?')[:3]
        context = {
            'prods': prod,
            'cat': categories,
        }
        return render(request, 'mainapp/main.html', context=context)


def cart_detail(request):
    cart = Cart(request)
    cart_form = CartAddProductForm()
    return render(request, 'mainapp/blocks/header.html', {
        'cart': cart,
        'cart_product_form': cart_form
    })


def contact(request):
    return render(request, 'mainapp/plug.html', context={})


def about(request):
    return render(request, 'mainapp/plug.html', context={})
