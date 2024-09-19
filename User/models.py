from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    email = models.EmailField(unique=True, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_code = models.CharField(
        max_length=5, 
        blank=True, 
        null=True
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True
    )
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Users'

    def __str__(self):
        return f"{self.username}"