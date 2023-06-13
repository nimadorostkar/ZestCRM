from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Province, City


class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
admin.site.register(Province, ProvinceAdmin)


class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ['name', 'province']
    list_filter = ("province",)
    raw_id_fields = ('province'),
admin.site.register(City, CityAdmin)

