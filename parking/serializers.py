from rest_framework import serializers
from .models import ParkingSlot, ParkingReservation

class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = '__all__'

class ParkingReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingReservation
        fields = '__all__'
