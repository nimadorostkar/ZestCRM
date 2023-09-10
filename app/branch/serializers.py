from rest_framework import serializers
from .models import Branch
from authentication.models import User
from city.serializers import CitySerializer


class UserLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'is_active', 'is_first_login', 'national_code', 'first_name', 'last_name', 'position',
                  'phone', 'email', 'birthdate', 'address', 'city', 'province']



class BranchSerializer(serializers.ModelSerializer):
    branch_manager = UserLimitSerializer(required=False)
    branch_seller = UserLimitSerializer(required=False)
    city = CitySerializer(required=False)
    class Meta:
        model = Branch
        fields = '__all__'


class BranchSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'