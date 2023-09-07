from .models import Branch
from .serializers import BranchSerializer, BranchSimpleSerializer
from authentication.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from city.models import City


class Branches(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        serializer = BranchSerializer(Branch.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CreateBranch(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.user.position == 'مدیر فروش' or 'مدیر کل':
            data = request.data
            data['password'] = '12345678'
            data['position'] = 'مدیر شعبه'
            user_serializer = UserSerializer(data=data)
            if user_serializer.is_valid():
                user_serializer.save()
                user = User.objects.get(id=user_serializer.data['id'])
                user.set_password(request.data['password'])
                user.save(update_fields=['password'])
                data['branch_manager'] = user.id
                serializer = BranchSimpleSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=user_serializer.errors)
        else:
            return Response('فقط مدیرکل و مدیرفروش امکان ایجاد دارد' ,status=status.HTTP_406_NOT_ACCEPTABLE)





class AddSellerBranch(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.user.position == 'مدیر شعبه' or 'مدیر کل':
            data = request.data
            if Branch.objects.get(id=data['branch']).branch_manager == request.user:
                data['password'] = '12345678'
                data['position'] = 'فروشنده'
                user_serializer = UserSerializer(data=data)
                if user_serializer.is_valid():
                    user_serializer.save()
                    user = User.objects.get(id=user_serializer.data['id'])
                    user.set_password(request.data['password'])
                    user.save(update_fields=['password'])
                    try:
                        branch = Branch.objects.get(id=data['branch'])
                        branch.branch_seller = user
                        branch.save()
                        return Response('فروشنده افزوده شد', status=status.HTTP_200_OK)
                    except:
                        return Response('شعبه پیدا نشد یا مشکلی پیش آمده', status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=user_serializer.errors)
            else:
                return Response('فقط مدیر این شعبه امکان این کار را دارد' ,status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response('فقط مدیرکل و مدیرشعبه امکان ایجاد دارد' ,status=status.HTTP_406_NOT_ACCEPTABLE)







class BranchItem(APIView):
    serializer_class = BranchSimpleSerializer
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        branch = Branch.objects.get(id=self.kwargs["id"])
        serialized_data = self.serializer_class(branch).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    def patch(self, request, *args, **kwargs):
        branch = Branch.objects.get(id=self.kwargs["id"])
        serializer = BranchSimpleSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        branch = Branch.objects.get(id=self.kwargs["id"])
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
