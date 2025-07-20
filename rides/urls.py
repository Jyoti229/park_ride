from django.urls import path
from . import views

app_name = 'rides'

urlpatterns = [
    path('', views.ride_list, name='ride_list'),          # /rides/
    path('book/', views.ride_booking, name='ride_booking')
]
