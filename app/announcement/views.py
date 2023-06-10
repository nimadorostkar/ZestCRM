from authentication.models import User
from announcement.models import Announcement
from django.http import JsonResponse
from .serializers import AnnouncementSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
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
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.db.models import Q




class Announcements(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        data['user'] = request.user.id
        serializer = AnnouncementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            resp = {'status':'موفقیت ثبت آگهی' , 'data':serializer.data}
            return Response(resp, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)




class AnnouncementsAccept(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request,  *args, **kwargs):
        try:
            announcements = Announcement.objects.get(id=request.data['announcement_id'])
            announcements.accepted = True
            announcements.save()
            return Response('موفقیت تأیید آگهی', status=status.HTTP_200_OK)
        except:
            return Response('something went wrong!', status=status.HTTP_406_NOT_ACCEPTABLE)



class AnnouncementsItem(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        announcement = Announcement.objects.get(id=self.kwargs["id"])
        req = request.data
        req['user'] = request.user.id
        serializer = AnnouncementSerializer(announcement, data=req)
        if serializer.is_valid():
            serializer.save()
            resp = {'status': 'موفقیت به‌روزرسانی آگهی', 'data': serializer.data}
            return Response(resp, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        announcements = Announcement.objects.get(id=request.data['announcement_id'])
        announcements.delete()
        return Response('موفقیت حذف آگهی' , status=status.HTTP_204_NO_CONTENT)



class Search(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        search = request.GET.get('query')
        searched_announcements = Announcement.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        serializer = AnnouncementSerializer(searched_announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





class AnnouncementsViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        announcement = Announcement.objects.get(id=self.kwargs["id"])
        return Response(announcement.views, status=status.HTTP_200_OK)



class MyAnnouncements(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.filter(user=request.user)
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
