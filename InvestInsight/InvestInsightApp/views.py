from django.contrib import messages 
from django.shortcuts import redirect, render
from .models import Investments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
        curr_val  = request.POST.get('curr-val')
        p_date = request.POST.get('p-date')
        notes = request.POST.get('notes')
        if investment_type == "":
            messages.error(request, "Please select a valid investment type.")
            return redirect("investments")
        investment = Investments.objects.create(investor=request.user,investment_type=investment_type,name=investment_name,invested_amount=investment_amt,purchase_date=p_date,current_value=curr_val,notes=notes)
    investment_data = Investments.objects.filter(investor=request.user)
    net = 0
    invested = 0
    for inv in investment_data:
        inv.gain_loss = inv.current_value - inv.invested_amount
        inv.gain_loss_percent = round( (inv.invested_amount/inv.current_value)*100,2)
        net += inv.current_value
        invested += inv.invested_amount
    return render(request,"dashboard.html",{"investment_data":investment_data,"net_worth":net,"invested":invested,"gain_loss":net-invested})