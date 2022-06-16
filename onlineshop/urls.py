from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('mainapp.urls')),
                  path('', include('detailsapp.urls')),
                  path('', include('filterprodapp.urls')),
                  path('', include('sendemail.urls')),
                  path('cart/', include('cartapp.urls', namespace='cart')),
                  path('orders/', include('ordersapp.urls', namespace='orders')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
