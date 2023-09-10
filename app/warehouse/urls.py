from django.urls import path
from warehouse import views


urlpatterns = [
    path('warehouses', views.Warehouses.as_view(), name='warehouses'),
    path('warehouse-item/<int:id>', views.WarehouseItem.as_view(), name='warehouse-item'),
]
