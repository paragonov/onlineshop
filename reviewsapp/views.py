from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from mainapp.models import Products
from reviewsapp.forms import AddReviewForm
from reviewsapp.models import Reviews


class LeaveReviewView(View):
    def get(self, request, *args, **kwargs):
        prod = Products.objects.get(url=kwargs['url'])
        form = AddReviewForm
        return render(request, 'reviewsapp/leave_review.html', context={
            'prod': prod,
            'form': form
        })

    def post(self, request, *args, **kwargs):
        if request.POST:
            form = AddReviewForm(request.POST)
            prod_id = Products.objects.filter(url=kwargs['url']).values('id')
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                rating = int(request.POST.get('rating'))
                comment = form.cleaned_data['comment']
                review_obj = Reviews(name=name, email=email, rating=rating, comment=comment, product_id=prod_id)
                review_obj.save()
                return HttpResponseRedirect('success')


class SuccessView(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'reviewsapp/success.html', {'prod': Products.objects.get(url=kwargs['url'])})
