from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.custom_usermanager import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


