from os import name
from django.contrib.auth import login, logout
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]