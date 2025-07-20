
from django.db import models

class Pricing(models.Model):
    SERVICE_CHOICES = [
        ('parking', 'Parking'),
        ('ride', 'Ride'),
    ]
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    peak_multiplier = models.FloatField(default=1.0)
    last_updated = models.DateTimeField(auto_now=True)

    def calculate_price(self, is_peak=False):
        return self.base_price * (self.peak_multiplier if is_peak else 1)


# Create your models here.
