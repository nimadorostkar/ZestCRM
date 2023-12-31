from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('api/', include('authentication.urls')),
    path('api/', include('dj_rest_auth.urls')),
    path('api/', include('city.urls')),
    path('api/', include('product.urls')),
    path('api/', include('warehouse.urls')),
    path('api/', include('branch.urls')),
    path('api/', include('landing.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
