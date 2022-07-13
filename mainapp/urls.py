from django.urls import path
from .views import MainView, contact, about

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('contacts/', contact, name='contacts'),
    path('about/', about, name='about'),
]