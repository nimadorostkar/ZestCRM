from django.db import models
from branch.models import Branch
from city.models import City, Province

class Warehouse(models.Model):
    is_central = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)

    inventory = models.IntegerField(default=0)
    gross_inventory = models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)
