from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def account(request):
    return render(request, 'account/login.html')

def login(request):
    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            print('radddiiiiiiiiiiiii')
            return redirect('index')
        else:
            print('ne radiiiiiiiiii')
            return redirect('account')
    


