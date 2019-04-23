from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
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
    return render(request, 'gamelobby/pvp.html')

@login_required(login_url='/log_in/')
def pvpnew(request):
    return render(request, 'gamelobby/pvp.html')

def activegame(request, room_name):
    return render(request, 'gamelobby/activegame.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })