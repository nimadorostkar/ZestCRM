from django.urls import path
from announcement import views

urlpatterns = [
    path('announcements', views.Announcements.as_view(), name='announcements'),
    path('announcements/<int:id>/accept', views.AnnouncementsAccept.as_view(), name='announcements_accept'),
    path('announcements/<int:id>', views.AnnouncementsItem.as_view(), name='announcements_item'),
    path('announcements/search', views.Search.as_view(), name='search'),
    path('announcements/<int:id>/views', views.AnnouncementsViews.as_view(), name='announcements_views'),
    path('my-announcements', views.MyAnnouncements.as_view(), name='my_announcements'),
]
