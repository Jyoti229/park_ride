
from django.contrib import admin
from .models import Ride

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('user', 'ride_type', 'pickup_point', 'drop_point', 'schedule_time', 'status')
    list_filter = ('ride_type', 'status')


# Register your models here.
