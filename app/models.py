from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=150, blank=False)
