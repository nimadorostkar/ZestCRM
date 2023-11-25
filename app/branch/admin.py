from django.contrib import admin
from .models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_manager', 'branch_seller', 'city', 'created_on')
    raw_id_fields = ('branch_manager'),
admin.site.register(Branch, BranchAdmin)

