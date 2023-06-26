from django.urls import path
from city import views

urlpatterns = [
    path('cities', views.Cities.as_view(), name='cities'),
    path('provinces', views.Provinces.as_view(), name='provinces'),

]
