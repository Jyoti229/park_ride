from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import viewsets  # type: ignore

from .models import Pricing
from .serializers import PricingSerializer
from rides.models import Ride

class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

# def payment(request):
#     ride_id = request.POST.get('ride_id')
#     ride = Ride.objects.get(id=ride_id)
#     amount = 500  # Example amount
#     return render(request, 'payment.html', {'ride': ride, 'amount': amount})

def payment(request):
    if request.method == 'GET':
        return render(request, 'payment.html', {'ride': None, 'amount': 500})  # dummy/default
    elif request.method == 'POST':
        ride_id = request.POST.get('ride_id')
        try:
            ride = Ride.objects.get(id=ride_id)
        except Ride.DoesNotExist:
            return HttpResponseBadRequest("Ride not found.")

        amount = 500
        return render(request, 'payment.html', {'ride': ride, 'amount': amount})
    else:
        return HttpResponseBadRequest("Invalid request method.")



def confirm_payment(request):
    if request.method == 'POST':
        ride_id = request.POST.get('ride_id')
        # Here you'd mark the ride as paid, store payment record, etc.
        print(f"Payment confirmed for ride ID: {ride_id}")
        return redirect('rides:ride_list')
    return HttpResponseBadRequest("Invalid request method.")



# def confirm_payment(request):
#     if request.method == 'POST':
#         ride_id = request.POST.get('ride_id')
#         # Payment logic (e.g., mark ride as paid)
#         return redirect('ride:ride_list')


def pricing_list(request):
    pricings = Pricing.objects.all()
    serializer = PricingSerializer(pricings, many=True)
    return JsonResponse(serializer.data, safe=False)

def pricing_detail(request, pk):
    try:
        pricing = Pricing.objects.get(pk=pk)
        serializer = PricingSerializer(pricing)
        return JsonResponse(serializer.data)
    except Pricing.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


# Create your views here.
