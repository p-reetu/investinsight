from django.contrib import admin
from .models import Expense, GoldRates, Investments

# Register your models here.
admin.site.register(Investments)
admin.site.register(GoldRates)
admin.site.register(Expense)