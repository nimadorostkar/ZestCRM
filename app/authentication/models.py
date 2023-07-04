from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.custom_usermanager import UserManager


class User(AbstractUser):
    CHOICES = (('مدیر کل', 'مدیر کل'),
               ('مدیر فروش', 'مدیر فروش'),
               ('مدیر استان', 'مدیر استان'),
               ('مدیر شعبه', 'مدیر شعبه'),
               (' فروشنده', ' فروشنده'),
               ('حسابدار', 'حسابدار'))
    username = None
    is_first_login = models.BooleanField(default=True)
    national_code = models.CharField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256,null=True, blank=True)
    position = models.CharField(max_length=256, choices=CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=256, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=256, unique=True, null=True, blank=True)
    birthdate = models.CharField(max_length=256, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = []

