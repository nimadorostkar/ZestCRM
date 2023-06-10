from rest_framework import serializers
from .models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256, allow_null=False)
    password = serializers.CharField(max_length=256, allow_null=False)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


