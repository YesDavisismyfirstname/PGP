from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from apps.game_window.models import Lobbies
import json

User = get_user_model()
# Create your views here.

@login_required(login_url='/log_in/')
def gamelobby(request):
    return render(request, 'gamelobby/gamemode.html')

@login_required(login_url='/log_in/')
def index(request):
    return render(request, 'gamelobby/gamelobby.html')

@login_required(login_url='/log_in/')
def pvp(request):
    ctx = {
        'rooms' : Lobbies.objects.order_by('name')
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

def activegame(request, room_name):
    return render(request, 'gamelobby/activegame.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })