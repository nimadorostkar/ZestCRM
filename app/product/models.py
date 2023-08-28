from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
