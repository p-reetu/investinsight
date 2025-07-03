from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeView),
    path('register/',views.registerView),
    path('login/',views.loginView),
    path('logout/',views.logoutView),
    path('investments',views.InvestmentView, name='investments'),
    path('expenses',views.ExpenseView, name='expenses'),
    path('delete/<int:id>',views.InvestmentDeletionView, name='delete_investment'),
]
