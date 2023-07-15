from django.urls import path
from branch import views

urlpatterns = [
    path('branches', views.Branches.as_view(), name='branches'),
    path('create-branch', views.CreateBranch.as_view(), name='create-branch'),
    path('add-seller-branch', views.AddSellerBranch.as_view(), name='add-seller-branch'),

]
