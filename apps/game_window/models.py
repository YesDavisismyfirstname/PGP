from django.db import models


    
class Pokemon(models.Model):
    name=models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    height = models.IntegerField()
    width = models.IntegerField()
    # animation = animation for pokemon
    # sound = sound for pokemon
    
    # enemy pokemon = manytomany with levels table
    ability = models.ManyToManyField(Abilities, releated_name='pokemon')
    # collection = manytomany with player
    
class Abilities(models.Model):
    name = models.CharField(max_length=45)
    power = models.InegerField()
    #animation = move animation
    #sound = move sound
    
class Player(models.Model):
    name = models.CharField(max_length=45)
    level = IntegerField()
    collected = models.ManyToManyField(Pokemon, related_name='player')
    lobby = models.ForeignKey(Lobbies, related_name='player')
    riding = models.ForeignKey(Poke_Rider, related_name='player')    
    
class Poke_Rider(Pokemon):
    height = models.IntegerField()
    width = models.IntegerField()
    start_pos = models.IntegerField()
    # additional_abilities = manytomany with abilities table
    
class Lobbies(models.Model):
    name = models.CharField(max_length=45)
    max_players= models.IntegerField()
    # ref to the map lvl
    map = models.CharField(max_length=255, null=True)  
    
class Levels():
    pass
        
    
    
    
    
    
    
    
    
