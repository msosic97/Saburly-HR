from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import LoginForm

# Create your views here.
def getLogin(request):
    
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
            return redirect('getLogin')

