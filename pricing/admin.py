
from django.contrib import admin
from .models import Pricing

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'base_price', 'peak_multiplier', 'last_updated')
    list_filter = ('service_type',)


# Register your models here.
