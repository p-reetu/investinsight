from decimal import Decimal
import json
from django.contrib import messages 
from django.shortcuts import get_object_or_404, redirect, render
from .models import Investments, GoldRates
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date, datetime
from django.db.models import Sum
from django.core.serializers.json import DjangoJSONEncoder

def registerView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return render(request, "register.html")
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('investments')
    return render(request,"register.html")

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('investments')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")
    return render(request,"login.html")

def logoutView(request):
    if request.method == "POST":
        logout(request)
    return render(request,"login.html")

@login_required
def InvestmentView(request):
    if request.method == "POST":
        investment_type  = request.POST.get('inv-type')
        investment_name  = request.POST.get('inv-name')
        investment_amt  = request.POST.get('inv-amt')
        if investment_type == "Gold":
            curr_per_gram = GoldRates.objects.all().order_by('-date').first()
            investment_grams = Decimal(request.POST.get('gram-field'))
            curr_val = curr_per_gram.rate*investment_grams
        else:
            curr_val  = request.POST.get('curr-val')
        p_date = request.POST.get('p-date')
        notes = request.POST.get('notes')
        hasErrors = False
        if int(investment_amt) <= 0:
            messages.error(request, "Please add a valid investment amount.")
            hasErrors = True
        if date.today() < datetime.strptime(p_date, "%Y-%m-%d").date():
            messages.error(request, "Please add past purchase date")
            hasErrors = True
        if hasErrors:
            return redirect("investments")
        investment = Investments.objects.create(investor=request.user,investment_type=investment_type,name=investment_name,invested_amount=investment_amt,purchase_date=p_date,current_value=curr_val,notes=notes)
    investment_data = Investments.objects.filter(investor=request.user).order_by('investment_type','-current_value')
    net = 0
    invested = 0
    total_current_value = 0
    short_term_holdings = []
    long_term_holdings = []
    for inv in investment_data:
        inv.gain_loss = inv.current_value - inv.invested_amount
        inv.gain_loss_percent = round((inv.gain_loss / inv.invested_amount) * 100, 2)
        if (date.today()-inv.purchase_date).days>=365:
            long_term_holdings.append(inv)
        else:
            short_term_holdings.append(inv)
        net += inv.current_value
        invested += inv.invested_amount
        total_current_value += inv.current_value

    #Diversification Insight
    DI = Investments.objects.filter(investor=request.user).values('investment_type').annotate(
        total_invested=Sum('invested_amount'),
        total_current=Sum('current_value')
    )
    wellDiversified = True
    for item in DI:
        item['total_invested_perc'] = round((item['total_invested'] / invested) * 100, 2)
        if item['total_invested_perc']>=60:
            wellDiversified = False

    #goldrate chart
    goldrates = GoldRates.objects.all().order_by('date')
    dates = []
    rates = []
    for ele in goldrates:
        dates.append(ele.date.strftime("%m-%d-%Y"))
        rates.append(float(ele.rate))
    return render(request,"dashboard.html",{
        "investment_data":investment_data,
        "net_worth":net,"invested":invested,
        "total_current_value":total_current_value,
        "gain_loss":net-invested,
        "DI":DI,"wellDiversified":wellDiversified,
        "profit":net-invested>0,
        "short_term_holdings":short_term_holdings,
        "long_term_holdings":long_term_holdings,
        "gold_dates":json.dumps(dates, cls=DjangoJSONEncoder),
        "gold_rates":json.dumps(rates)
        })

@login_required
def InvestmentDeletionView(request,id):
    investment = get_object_or_404(Investments, id=id, investor=request.user)
    investment.delete()
    return redirect("investments")