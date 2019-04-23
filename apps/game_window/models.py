from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Abilities(models.Model):
    name = models.CharField(max_length=45)
    power = models.IntegerField()
    #animation = move animation
    #sound = move sound

class Pokemon(models.Model):
    name = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    height = models.IntegerField()
    width = models.IntegerField()
    # animation = animation for pokemon
    # sound = sound for pokemon    
    ability = models.ManyToManyField(Abilities, related_name='pokemon')

class Levels(models.Model):
    name = models.CharField(max_length=45)
    image = models.FilePathField(path="/apps/login/static/login/images/levels")
    levelmap ={}
    enemy = models.ManyToManyField(Pokemon, related_name='level')
    
class Lobbies(models.Model):
    name = models.CharField(max_length=45)
    max_players= models.IntegerField()
    created_by = models.ForeignKey(User)
    # ref to the map lvl
    level = models.ForeignKey(Levels, related_name='lobby', null=True) 
    
class Poke_Rider(Pokemon):
    start_pos = models.IntegerField()
    # additional_abilities = manytomany with abilities table
    
class Player(models.Model):
    name = models.CharField(max_length=45)
    level = models.IntegerField()
    collected = models.ManyToManyField(Pokemon, related_name='playerCollected')
    lobby = models.ForeignKey(Lobbies, related_name='player')
    riding = models.ForeignKey(Poke_Rider, related_name='player')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user',on_delete=models.PROTECT, null=True)  
    

    
    
    
    
    
