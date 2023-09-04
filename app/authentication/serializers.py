from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.Serializer):
    national_code = serializers.CharField(max_length=256, allow_null=False)
    password = serializers.CharField(max_length=256, allow_null=False)

class SignUpSerializer(serializers.ModelSerializer):
    national_code = serializers.CharField(max_length=256, allow_null=False)
    password = serializers.CharField(max_length=256, allow_null=False)
    class Meta:
        model = User
        fields = ['national_code', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'is_active', 'is_first_login', 'national_code', 'first_name', 'last_name', 'position',
                  'phone', 'email', 'birthdate', 'address', 'city', 'province']
