from django.db import models
from branch.models import Branch
from city.models import City

class Warehouse(models.Model):
    is_central = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
