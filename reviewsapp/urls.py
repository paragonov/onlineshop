from django.urls import path
from .views import LeaveReviewView, SuccessView

urlpatterns = [
    path('products/<slug:url>/review/', LeaveReviewView.as_view(), name='review'),
    path('products/<slug:url>/review/success', SuccessView.as_view(), name='success'),
]