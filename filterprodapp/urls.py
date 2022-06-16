from django.urls import path
from .views import FilterProdView

urlpatterns = [
    path('products/', FilterProdView.as_view(), name='filter_prod'),
]