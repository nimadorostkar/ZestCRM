from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('national_code', 'position', 'updated_on', 'created_on')
    list_filter = ('position', 'updated_on', 'created_on')
    search_fields = ['national_code', 'username']
admin.site.register(User, UserAdmin)

