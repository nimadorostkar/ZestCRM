from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.custom_usermanager import UserManager


class Warehouse(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name="نام")
    def __str__(self):
        return str(self.name)
