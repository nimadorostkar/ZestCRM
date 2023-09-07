from django.db import models
from warehouse.models import Warehouse


class Product(models.Model):
    product_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    cash_sales = models.IntegerField(default=0)
    non_cash_sales = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)



class FirstPeriodProduct (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.product) +' | '+ str(self.qty)
