from django.db import models

    
class Abilities(models.Model):
    name = models.CharField(max_length=45)
    power = models.IntegerField()
    
    
    
class Pokemon(models.Model):
    name=models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    height = models.IntegerField()
    width = models.IntegerField()   
    ability = models.ManyToManyField(Abilities, related_name='pokemon')
    
class Levels(models.Model):
    name = models.CharField(max_length=45)
    map ={}
    enemy = models.ManyToManyField(Pokemon, related_name='level')
   
class Lobbies(models.Model):
    name = models.CharField(max_length=45)
    max_players= models.IntegerField()
    # ref to the map lvl
    level = models.ForeignKey(Levels, related_name='lobby',on_delete=models.PROTECT)

class Poke_Rider(Pokemon):    
    start_pos = models.IntegerField()
    # additional_abilities = manytomany with abilities table
    
class Player(models.Model):
    name = models.CharField(max_length=45)
    level = models.IntegerField()
    collected = models.ManyToManyField(Pokemon, related_name='player_c')
    lobby = models.ForeignKey(Lobbies, related_name='player_l',on_delete=models.PROTECT)
    riding = models.ForeignKey(Poke_Rider, related_name='player_r',on_delete=models.PROTECT)    
    

    

    

    
        
    
    
    
    
    
    
    
    
