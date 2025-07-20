from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets  # type: ignore
from .models import ParkingSlot, ParkingReservation
from .serializers import ParkingSlotSerializer, ParkingReservationSerializer

class ParkingSlotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer

class ParkingReservationViewSet(viewsets.ModelViewSet):
    queryset = ParkingReservation.objects.all()
    serializer_class = ParkingReservationSerializer

# Template-based views
def parking_list(request):
    parking_slots = ParkingSlot.objects.all()
    return render(request, 'parking_list.html', {'parking_slots': parking_slots})

def parking_detail(request, pk):
    parking_slot = get_object_or_404(ParkingSlot, pk=pk)
    return render(request, 'parking_detail.html', {'parking_slot': parking_slot})

def parking_booking(request):
    """Render the parking booking page."""
    return render(request, 'parking_booking.html')
