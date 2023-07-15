from django.db import models
from authentication.models import User
from city.models import City


class Branch(models.Model):
    is_central = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    branch_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    branch_seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='branch_seller', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.city) + str(self.branch_manager.first_name) + str(self.branch_manager.last_name)
