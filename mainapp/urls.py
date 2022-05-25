from django.urls import path
from .views import MainView, SelectCatView, ProductsView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('products/', SelectCatView.as_view(), name='filter_prod'),
]