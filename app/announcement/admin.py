from django.contrib import admin
from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'content', 'updated_on', 'created_on', 'views', 'accepted')
    list_filter = ('accepted', 'user', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
admin.site.register(Announcement, AnnouncementAdmin)
