from os import name
from django.contrib.auth import logout
from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]