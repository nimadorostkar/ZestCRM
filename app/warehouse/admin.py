from django.contrib import admin
from .models import Warehouse

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'is_central')
admin.site.register(Warehouse, WarehouseAdmin)

