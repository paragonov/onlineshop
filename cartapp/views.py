from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Products
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, url):
    cart = Cart(request)
    product = get_object_or_404(Products, url=url)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("cart:cart_detail")


def cart_remove(request, url):
    cart = Cart(request)
    product = get_object_or_404(Products, url=url)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cartapp/detail.html", {"cart": cart})
