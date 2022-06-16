from django.db.models import Count, Q
from django.views.generic import DetailView, ListView

from cartapp.forms import CartAddProductForm
from mainapp.models import Products, Brands, Categories
from detailsapp.models import Reviews


class FilterProdView(ListView):
    paginate_by = 12
    template_name = 'filterprodapp/filter_prod.html'
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
