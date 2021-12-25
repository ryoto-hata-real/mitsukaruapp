from django.contrib import admin
from django.urls import path, include
from mainapp import views
from product import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mainapp.urls')),
    path('mainapp/', include('mainapp.urls')),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)