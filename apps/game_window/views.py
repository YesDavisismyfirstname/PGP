from django.shortcuts import render
from apps.game_window.models import Lobbies, Player
import json
from django.utils.safestring import mark_safe
from django.core import serializers

def gamewindow(request):
    return render(request, 'game_window/render.html')


def launchgame(request, room_id):
    lobby = Lobbies.objects.get(id=room_id)
    players =  serializers.serialize('json', lobby.player.all(), fields=('user',))
    ctx = {
        "players" : players,
    }
    return render(request, 'game_window/render.html',ctx)
