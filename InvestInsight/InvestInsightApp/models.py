from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Investments(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=100)  # e.g., Stock, Mutual Fund, Crypto
    name = models.CharField(max_length=255)  # e.g., Reliance, Bitcoin
    invested_amount = models.DecimalField(max_digits=15, decimal_places=2)  # In INR
    purchase_date = models.DateField()
    current_value = models.DecimalField(max_digits=15, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

class GoldRates(models.Model):
    date = models.DateField(auto_now_add=True)
    rate = models.DecimalField(max_digits=15, decimal_places=2)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_date  = models.DateField()
    expense_amt  = models.DecimalField(max_digits=15, decimal_places=2)
    expense_name  = models.CharField(max_length=255)
    expense_type  = models.CharField(max_length=100)