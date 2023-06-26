from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('sign-up', views.SignUp.as_view(), name='sign-up'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('change-pass', views.ChangePass.as_view(), name='change-pass'),
    path('create-sales-manager', views.CreateSalesManager.as_view(), name='create-sales-manager'),
    path('create-provincial-manager', views.CreateProvincialManager.as_view(), name='create-provincial-manager'),
]
