from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(models.Model):
    
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  
  def __str__(self):
      return self.email
