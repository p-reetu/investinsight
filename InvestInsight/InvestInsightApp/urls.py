from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerView),
    path('login/',views.loginView),
    path('logout/',views.logoutView),
    path('investments',views.InvestmentView, name='investments'),
]
