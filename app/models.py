from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=25, null=True)
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField(
        null=False, blank=False, default="avatar.png", upload_to='images/')

    USERNAME_FIELDS = "email"
    REQUIRED_FIELDS = []


class Link(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
