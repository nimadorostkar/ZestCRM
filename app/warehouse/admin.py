from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'updated_on', 'created_on')
    list_filter = ('updated_on', 'created_on')
    search_fields = ['email', 'username']
admin.site.register(User, UserAdmin)

