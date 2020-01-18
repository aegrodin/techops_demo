from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Response(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    color = models.CharField(max_length=100)
    pet = models.CharField(max_length=100)
