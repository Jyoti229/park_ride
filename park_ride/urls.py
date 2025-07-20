from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter  # type: ignore
from parking.views import ParkingSlotViewSet, ParkingReservationViewSet
from rides.views import RideViewSet
from pricing.views import PricingViewSet
from park_ride import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView


router = DefaultRouter()
router.register('parking-slots', ParkingSlotViewSet)
router.register('parking-reservations', ParkingReservationViewSet)
router.register('rides', RideViewSet)
router.register('pricing', PricingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # All API endpoints
    path('', views.home, name='home'),  # Default home page
    path('rides/', include('rides.urls')),
    path('parking/', include('parking.urls')),
    path('pricing/', include('pricing.urls')),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
