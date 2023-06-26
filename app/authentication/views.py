from .models import User
from .serializers import LoginSerializer, UserSerializer, SignUpSerializer
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
            return Response('username or password is incorrect or something wrong.  [ {} ]'.format(repr(e)), status=status.HTTP_406_NOT_ACCEPTABLE)


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
        user = User.objects.get(id=request.user.id)
        user.set_password( request.data['password'] )
        user.save(update_fields=['password'])
        return Response('change password done', status=status.HTTP_200_OK)


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
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        else:
            return Response('فقط مدیرکل و مدیرفروش امکان ایجاد دارد' ,status=status.HTTP_406_NOT_ACCEPTABLE)
