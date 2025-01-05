from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name
