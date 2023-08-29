from django.urls import path
from product import views

urlpatterns = [
    path('product', views.Product.as_view(), name='product'),
    path('product/<int:id>', views.ProductItem.as_view(), name='product_item'),
]
