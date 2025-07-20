from django.shortcuts import render
from rest_framework import viewsets # type: ignore
from .models import Ride
from .serializers import RideSerializer

# API ViewSet for REST Framework
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

# Template-based views for frontend
def ride_list(request):
    return render(request, 'rides/ride_list.html')  # Ensure template is inside rides/templates/rides/

def ride_booking(request):
    return render(request, 'rides/ride_booking.html')


# Create your views here.
