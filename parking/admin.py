from django.contrib import admin
from django.contrib import admin
from .models import ParkingSlot, ParkingReservation

@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('station', 'slot_number', 'is_available')
    list_filter = ('station', 'is_available')

@admin.register(ParkingReservation)
class ParkingReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'start_time')


# Register your models here.
