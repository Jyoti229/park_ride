from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    loyalty_points = models.IntegerField(default=0)
    subscription_plan = models.CharField(
        max_length=20, 
        choices=[('basic', 'Basic'), ('premium', 'Premium')],
        default='basic'
    )
    
    def __str__(self):
        return self.username
