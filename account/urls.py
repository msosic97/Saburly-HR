from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login', views.login, name='login')
]