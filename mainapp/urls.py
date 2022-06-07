from django.urls import path
from .views import MainView, FilterProdView, DetailProdView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('products/', FilterProdView.as_view(), name='filter_prod'),
    path('products/<slug:url>/', DetailProdView.as_view(), name='detail_prod')
]