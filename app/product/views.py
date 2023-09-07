from product import models
from .serializers import ProductSerializer, FirstProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView


class Product(APIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        serialized_data = self.serializer_class(products, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductItem(APIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        product = models.Product.objects.get(id=self.kwargs["id"])
        serialized_data = self.serializer_class(product).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    def patch(self, request, *args, **kwargs):
        product = models.Product.objects.get(id=self.kwargs["id"])
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        product = models.Product.objects.get(id=self.kwargs["id"])
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class FirstPeriodProduct(APIView):
    serializer_class = FirstProductSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        products = models.FirstPeriodProduct.objects.all()
        serialized_data = self.serializer_class(products, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FirstProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



