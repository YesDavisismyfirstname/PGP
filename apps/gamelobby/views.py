from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from apps.game_window.models import Room
from apps.gamelobby.forms import newLobby
from django.urls import reverse
from django.shortcuts import render, redirect

User = get_user_model()
# Create your views here.




@login_required(login_url='/log_in/')
def gamelobby(request):
    return render(request, 'gamelobby/gamemode.html')

@login_required(login_url='/log_in/')
def pvp(request):
    ctx = {
        'rooms' : Room.objects.order_by('name')
        }
    return render(request, 'gamelobby/index.html', ctx)

@login_required(login_url='/log_in/')
def pvpNew(request):
    if request.method=="POST":
        newlob = newLobby(request.POST)
        if newlob.is_valid():
            newlob.save()
            return redirect('/gamelobby/pvp')
        else: 
            ctx = {
                'lobby' : newlob
            }
            return render(request, 'gamelobby/pvpnew.html',ctx)
    else:
        lobby = newLobby()
        ctx = {
            'lobby' : lobby
            }
        return render(request, 'gamelobby/pvpnew.html', ctx)
