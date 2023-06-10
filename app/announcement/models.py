from django.db import models
from authentication.models import User


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    accepted = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=1000)
    views = models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


