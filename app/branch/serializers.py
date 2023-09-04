from rest_framework import serializers
from .models import Branch
from authentication.serializers import UserLimitSerializer

class BranchSerializer(serializers.ModelSerializer):
    branch_manager = UserLimitSerializer()
    branch_seller = UserLimitSerializer()
    class Meta:
        model = Branch
        fields = '__all__'

