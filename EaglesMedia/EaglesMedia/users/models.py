from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
