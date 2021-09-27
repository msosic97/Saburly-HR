from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from cards.forms import CardForm
from cards.models import Card

# Create your views here.
@login_required
def dashboard(request):
    if request.method == 'POST':
        cardForm = CardForm(request.POST)
        if cardForm.is_valid():
            return redirect('cardsubmit')
    else:
        cardForm = CardForm()

    return render(request, 'account/dashboard.html', {'cardForm': cardForm})

def submitCard(request):
    if request.method == 'POST':
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        description = request.POST['description']
        # Check dates
        if Card.objects.filter(date_from=date_from, date_to=date_to).exists():
            print('Kartica vec postoji!')
            return redirect('dashboard')
            
        else:
            card = Card.objects.create(user = request.user, date_from=date_from, date_to=date_to, description=description)
            card.save()
            print('Kartica uspjesno kreirana!')
            return redirect('dashboard')

    else:
        return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == 'POST':
        #user logout
        auth.logout(request)
        return redirect('/')