from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('sign-up', views.SignUp.as_view(), name='sign-up'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('change-pass', views.ChangePass.as_view(), name='change-pass'),
    path('create-sales-manager', views.CreateSalesManager.as_view(), name='create-sales-manager'),
    path('create-provincial-manager', views.CreateProvincialManager.as_view(), name='create-provincial-manager'),
    path('sale-manager-list', views.SaleManagerList.as_view(), name='sale-manager-list'),
    path('sale-manager-list/<int:id>', views.SaleManagerList.as_view(), name='sale-manager-list'),
    path('province-manager-list', views.ProvinceManagerList.as_view(), name='province-manager-list'),
    path('province-manager/<int:id>', views.ProvinceManagerList.as_view(), name='province-manager'),
    path('sellers', views.Sellers.as_view(), name='sellers'),
]
