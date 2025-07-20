# rides/models.py
from django.db import models
from django.conf import settings

class Ride(models.Model):
    RIDE_TYPES = [
        ('cab', 'Cab'),
        ('shuttle', 'Shuttle'),
        ('e_rickshaw', 'E-Rickshaw'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ride_type = models.CharField(max_length=20, choices=RIDE_TYPES)
    pickup_point = models.CharField(max_length=100)
    drop_point = models.CharField(max_length=100)
    schedule_time = models.DateTimeField()
    is_shared = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.ride_type} - {self.pickup_point} to {self.drop_point}"


# Create your models here.
