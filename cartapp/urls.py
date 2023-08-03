from django.urls import path
from .views import cart_add, cart_detail, cart_remove

app_name = "cartapp"

urlpatterns = [
    path("", cart_detail, name="cart_detail"),
    path("add/<url>", cart_add, name="cart_add"),
    path("remove/<url>", cart_remove, name="cart_remove"),
]
