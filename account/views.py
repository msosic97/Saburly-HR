from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

def logout(request):
    if request.method == 'POST':
        #user logout
        auth.logout(request)
        return redirect('/')