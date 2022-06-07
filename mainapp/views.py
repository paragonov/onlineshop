
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from el_pagination.views import AjaxListView

from cartapp.forms import CartAddProductForm
from reviewsapp.models import Reviews
from .models import Categories, Products, Brands, Image


class MainView(View):

    def get(self, request, *args, **kwargs):
        prod = Products.objects.order_by('?')[:6]
        categories = Categories.objects.order_by('?')[:3]
        context = {
            'prods': prod,
            'cat': categories,
        }
        return render(request, 'mainapp/main.html', context=context)


class FilterProdView(ListView):
    paginate_by = 4
    template_name = 'mainapp/filter_prod.html'
    context_object_name = 'results'

    def get_queryset(self):
        result = []
        if self.request.GET:
            p_min = self.request.GET.get('price-min')
            p_max = self.request.GET.get('price-max')
            brand_list = self.request.GET.getlist('brand')
            cat_list = self.request.GET.getlist('cat')
            disc_bool = self.request.GET.get('disc')
            show = self.request.GET.get('show')
            if show:
                prod = Products.objects.all()[:int(show)]
            prod = Products.objects.all()
            if brand_list and cat_list:
                for c in cat_list:
                    for b in brand_list:
                        if disc_bool:
                            queryset = prod.filter(
                                Q(category__name=c) &
                                Q(brand__name=b) &
                                Q(discount=disc_bool) &
                                Q(price__range=(p_min, p_max)))
                            result.extend(queryset)
                        else:
                            queryset = prod.filter(
                                Q(category__name=c) &
                                Q(brand__name=b) &
                                Q(price__range=(p_min, p_max)))
                            result.extend(queryset)
                return result
            elif brand_list and disc_bool:
                for b in brand_list:
                    queryset = prod.filter(
                        Q(brand__name=b) & Q(discount=disc_bool) &
                        Q(price__range=(int(p_min), int(p_max))))
                    result.extend(queryset)
                return result
            elif cat_list and disc_bool:
                for c in cat_list:
                    queryset = prod.filter(
                        Q(category__name=c) & Q(discount=disc_bool) &
                        Q(price__range=(int(p_min), int(p_max))))
                    result.extend(queryset)
                return result
            elif (brand_list or cat_list) or disc_bool:
                queryset = prod.filter(
                    (Q(category__name__in=cat_list) |
                     Q(brand__name__in=brand_list) |
                     Q(discount=disc_bool)) &
                    Q(price__range=(int(p_min), int(p_max))))
                result.extend(queryset)
                return result
            elif p_min and p_max:
                queryset = prod.filter(Q(price__range=(int(p_min), int(p_max))))
                result.extend(queryset)
                return result
        queryset = Products.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brands.objects.values('name').annotate(bcount=Count('products')).order_by()
        context['cats'] = Categories.objects.values('name').annotate(ccount=Count('products')).order_by()
        context['disc'] = Products.objects.values('discount').annotate(dcount=Count('discount')).order_by()
        if self.request.GET:
            context['fc'] = self.request.GET.getlist('cat')
            context['fb'] = self.request.GET.getlist('brand')
            context['fd'] = self.request.GET.get('disc')
            context['fs'] = self.request.GET.get('show')
        return context


class DetailProdView(DetailView):
    model = Products
    template_name = 'mainapp/detail_prod.html'
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


