from django.contrib import admin
from .models import GoldRates, Investments

# Register your models here.
admin.site.register(Investments)
admin.site.register(GoldRates)