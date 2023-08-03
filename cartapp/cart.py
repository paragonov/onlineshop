from decimal import Decimal
from django.conf import settings
from mainapp.models import Products


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_url = str(product.url)
        if product_url not in self.cart:
            self.cart[product_url] = {"quantity": 0, "price": str(product.price)}
        if update_quantity:
            self.cart[product_url]["quantity"] = quantity
        else:
            self.cart[product_url]["quantity"] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_url = str(product.url)
        if product_url in self.cart:
            del self.cart[product_url]
            self.save()

    def __iter__(self):
        product_urls = self.cart.keys()
        products = Products.objects.filter(url__in=product_urls)
        for product in products:
            self.cart[str(product.url)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def get_total_len(self):
        return sum([item["quantity"] for item in self.cart.values()])

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
