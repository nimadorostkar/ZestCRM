from rest_framework import serializers
from .models import Branch
from authentication.models import User



class UserLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'is_active', 'is_first_login', 'national_code', 'first_name', 'last_name', 'position',
                  'phone', 'email', 'birthdate', 'address', 'city', 'province']




class BranchSerializer(serializers.ModelSerializer):
    branch_manager = UserLimitSerializer()
    branch_seller = UserLimitSerializer()
    class Meta:
        model = Branch
        fields = '__all__'


class BranchSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'