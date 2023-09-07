from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    cash_sales = models.IntegerField(default=0)
    non_cash_sales = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
