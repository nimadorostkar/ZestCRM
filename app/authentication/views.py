from .models import User
from .serializers import LoginSerializer, UserSerializer, SignUpSerializer, UserLimitSerializer, SellersSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status, pagination, mixins
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from branch.models import Branch
from branch.serializers import BranchSimpleSerializer
from warehouse.models import Warehouse
from city.models import Province
from branch.serializers import BranchSerializer
from warehouse.serializers import WarehouseSerializer


class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        try:
            user = authenticate(request, national_code=data['national_code'], password=data['password'])
            login(request, user)
            token = RefreshToken.for_user(user)
            token_response = { "refresh": str(token), "access": str(token.access_token) }
            response = { 'token':token_response , 'user':UserSerializer(user).data }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response('نام کاربری یا رمز عبور نادرست است یا چیزی اشتباه است.  [ {} ]'.format(repr(e)), status=status.HTTP_406_NOT_ACCEPTABLE)


class SignUp(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)

class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePass(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        user.set_password(request.data['password'])
        user.save(update_fields=['password'])
        user.is_first_login = False
        user.save()
        return Response('تغییر رمز عبور انجام شد', status=status.HTTP_200_OK)


class CreateSalesManager(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.user.position == 'مدیر کل':
            data = request.data
            data['position'] = 'مدیر فروش'
            data['password'] = '12345678'
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(id=serializer.data['id'])
                user.set_password(request.data['password'])
                user.save(update_fields=['password'])
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        else:
            return Response('فقط مدیرکل امکان ایجاد دارد' ,status=status.HTTP_406_NOT_ACCEPTABLE)

class CreateProvincialManager(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.user.position == 'مدیر فروش' or 'مدیر کل':
            data = request.data
            data['position'] = 'مدیر استان'
            data['password'] = '12345678'
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(id=serializer.data['id'])
                user.set_password(request.data['password'])
                user.save(update_fields=['password'])

                branch = Branch()
                branch.is_central = True
                branch.name = 'شعبه مرکزی استان'
                branch.address = data['address']
                branch.branch_manager = user
                branch.save()

                warehouse = Warehouse()
                warehouse.is_central = True
                warehouse.name = 'انبار مرکزی استان'
                warehouse.address = data['address']
                warehouse.branch = branch
                warehouse.province = Province.objects.get(id=data['province'])
                warehouse.save()

                response_data = {"user":serializer.data, "warehouse":WarehouseSerializer(warehouse).data, "branch":BranchSerializer(branch).data}

                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        else:
            return Response('فقط مدیرکل و مدیرفروش امکان ایجاد دارد' ,status=status.HTTP_406_NOT_ACCEPTABLE)




class SaleManagerList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.filter(position='مدیر فروش'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response('کاربر حذف شد',status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id=None):
        request.data['user'] = User.objects.get(id=id)
        request.data['password'] = User.objects.get(id=id).password
        request.data['national_code'] = User.objects.get(id=id).national_code
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ProvinceManagerList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.filter(position='مدیر استان'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        user = User.objects.get(id=id)
        user.delete()
        return Response('کاربر حذف شد',status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id=None):
        request.data['user'] = User.objects.get(id=id)
        request.data['password'] = User.objects.get(id=id).password
        request.data['national_code'] = User.objects.get(id=id).national_code
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Sellers(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        sellers = User.objects.filter(position='فروشنده')
        all_sellers = []
        for seller in sellers:
            #seller_item = SellersSerializer(seller).data
            branch = Branch.objects.filter(branch_seller=seller.id)
            branch_item = BranchSimpleSerializer(branch, many=True).data

            item = {'id':seller.id,'national_code':seller.national_code,'first_name':seller.first_name,'last_name':seller.last_name,
             'phone':seller.phone,'address':seller.address,'branch':branch_item,}

            #seller_item.append( {'branch':branch_item} )
            all_sellers.append(item)
        #serializer = SellersSerializer(User.objects.filter(position='فروشنده'), many=True)
        return Response(all_sellers, status=status.HTTP_200_OK)
