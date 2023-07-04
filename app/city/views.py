from .models import City, Province
from .serializers import ProvinceSerializer, CitySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView

class Provinces(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer = ProvinceSerializer(Province.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Cities(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer = CitySerializer(City.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)