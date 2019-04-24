from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from apps.game_window.models import Lobbies, Player
from apps.gamelobby.forms import newLobby
import json

User = get_user_model()
# Create your views here.

@login_required(login_url='/log_in/')
def gamelobby(request):
    return render(request, 'gamelobby/gamemode.html')

@login_required(login_url='/log_in/')
def pvp(request, room_name =""):
    if room_name != "":
        currentroom = Lobbies.objects.get(id=room_name)
        print(currentroom.name)
        activeplayers = currentroom.player.all()
        if request.user in activeplayers.__dict__:
            print("Yes")
        else:
            print("NO")
            print(activeplayers.values)
    try:
        active = Lobbies.objects.get(id=room_name)
    except:
        active = {}
    
    ctx = {
        'rooms' : Lobbies.objects.all(),
        'room_name_json': mark_safe(json.dumps(room_name)),
        'activeroom': active,
        }
    return render(request, 'gamelobby/pvp.html', ctx)

@login_required(login_url='/log_in/')
def pvpNew(request):
    if request.method=="POST":
        newlob = newLobby(request.POST)
        if newlob.is_valid():
            newlob.created_by = request.user
            newlob.save()
            request.user.logged_in_user.lobby = Lobbies.objects.last()
            request.user.logged_in_user.save()
            print(request.user.logged_in_user.__dict__)
            return redirect('/gamelobby/pvp')
        else: 
            ctx = {
                'lobby' : newlob
            }
            return render(request, 'gamelobby/pvpnew.html',ctx)
    else:
        lobby = newLobby(initial={'created_by': request.user})
        ctx = {
            'lobby' : lobby
            }
        return render(request, 'gamelobby/pvpnew.html', ctx)

def gamestart(request):
    return
# def activegame(request, room_name):
#     return render(request, 'gamelobby/pvp.html', {
#         'room_name_json': mark_safe(json.dumps(room_name)),
#         'active-room': room_name,
#     })