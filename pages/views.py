from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

