from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.pricing_list, name='pricing_list'),
    path('<int:pk>/', views.pricing_detail, name='pricing_detail'),
    path('checkout/', views.payment, name='checkout'),
    path('payment/', views.payment, name='payment'),  
    path('confirm/', views.confirm_payment, name='confirm_payment'),
]
