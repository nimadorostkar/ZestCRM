from django.contrib import admin
from .models import Product, FirstPeriodProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'product_id')
    search_fields = ['name',]
admin.site.register(Product, ProductAdmin)



class FirstPeriodProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'qty')
admin.site.register(FirstPeriodProduct, FirstPeriodProductAdmin)
