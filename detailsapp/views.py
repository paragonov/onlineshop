from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from cartapp.forms import CartAddProductForm
from mainapp.models import Products
from detailsapp.forms import AddReviewForm
from detailsapp.models import Reviews


class DetailProdView(DetailView):
    model = Products
    template_name = 'detailsapp/detail_prod.html'
    context_object_name = 'prod'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        rev_ojb = Reviews.objects.filter(product__url__icontains=self.kwargs['url']).order_by('-rating')
        if rev_ojb:
            count_rating_obj = 0
            sum_rating_obj = 0
            count_reviews = dict()
            for rating in sorted(range(1, 6), reverse=True):
                rating_obj = rev_ojb.filter(rating=rating)
                count_reviews[rating] = rating_obj.count()
                count_rating_obj += rating_obj.count()
                sum_rating_obj += rating_obj.count() * rating
            avg_rating = sum_rating_obj / count_rating_obj
            context['ar'] = round(avg_rating, 1)
            context['ar2'] = int(avg_rating)
            context['cr'] = rev_ojb.values('rating').annotate(rcount=Count('rating')).order_by('-rating')
            context['countrev'] = count_reviews
        context['rp'] = rev_ojb
        context['crp'] = rev_ojb.count()
        context['cart_product_form'] = CartAddProductForm()
        context['prods'] = Products.objects.order_by('?')[:4]

        return context


class LeaveReviewView(View):
    def get(self, request, *args, **kwargs):
        prod = Products.objects.get(url=kwargs['url'])
        form = AddReviewForm
        return render(request, 'detailsapp/leave_review.html', context={
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
    def get(self, request, *args, **kwargs):
        return render(request, 'detailsapp/success.html', {'prod': Products.objects.get(url=kwargs['url'])})
