
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone', 'loyalty_points', 'subscription_plan', 'is_staff')
    search_fields = ('username', 'email', 'phone')

admin.site.register(CustomUser, CustomUserAdmin)
