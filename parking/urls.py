from django.urls import path
from . import views

app_name = 'parking'

urlpatterns = [
    path('', views.parking_list, name='parking_list'),      # /parking/
    path('<int:pk>/', views.parking_detail, name='parking_detail'),
    path('book/', views.parking_booking, name='parking_booking'),
]
