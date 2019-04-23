from django import forms
from django.forms import ModelForm
from apps.game_window.models import Room    

class newLobby(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'max_players']
