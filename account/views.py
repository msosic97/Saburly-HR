from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
def account(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return redirect('login')
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form': form})


def login(request):
    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('account')

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

def logout(request):
    if request.method == 'POST':
        #user logout
        auth.logout(request)
        return redirect('/')
    


