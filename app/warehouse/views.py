from .models import Warehouse
from rest_framework.decorators import api_view, permission_classes
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
from .serializers import WarehouseSerializer



class Warehouses(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer = WarehouseSerializer(Warehouse.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class WarehouseItem(APIView):
    serializer_class = WarehouseSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        warehouse = Warehouse.objects.get(id=self.kwargs["id"])
        serialized_data = self.serializer_class(warehouse).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        warehouse = Warehouse.objects.get(id=self.kwargs["id"])
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        warehouse = Warehouse.objects.get(id=self.kwargs["id"])
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
