from rest_framework import serializers
from .models import Product, FirstPeriodProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FirstProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstPeriodProduct
        fields = '__all__'
