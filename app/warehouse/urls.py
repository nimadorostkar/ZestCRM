from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('sign-up', views.SignUp.as_view(), name='sign-up'),
    path('profile', views.Profile.as_view(), name='profile'),

]
