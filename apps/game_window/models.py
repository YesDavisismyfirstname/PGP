from django.conf import settings
from django.db import models
from channels import Group
import json
from django.utils.six import python_2_unicode_compatible

from apps.gamelobby.settings import MSG_TYPE_MESSAGE

@python_2_unicode_compatible
class Room(models.Model):
    name = models.CharField(max_length=45)
    max_players= models.IntegerField()
    # ref to the map lvl
    course_map = models.CharField(max_length=255, null=True) 
    def str(self):
        return self.name
    @property
    def websocket_group(self):
        return Group("room-%s" % self.id)
    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )

class Pokemon(models.Model):
    name=models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    height = models.IntegerField()
    width = models.IntegerField()
    # animation = animation for pokemon
    # sound = sound for pokemon
    
    # enemy pokemon = manytomany with levels table
    #ability = models.ManyToManyField(Abilities, releated_name='pokemon')
    # collection = manytomany with player
    
class Abilities(models.Model):
    name = models.CharField(max_length=45)
    power = models.IntegerField()
    #animation = move animation
    #sound = move sound
    
class Player(models.Model):
    name = models.CharField(max_length=45)
    level = models.IntegerField()
    collected = models.ManyToManyField(Pokemon, related_name='player')
    lobby = models.ForeignKey(Room, related_name='player')
    #riding = models.ForeignKey(Poke_Rider, related_name='player')    
    
class Poke_Rider(Pokemon):
    start_pos = models.IntegerField()
    # additional_abilities = manytomany with abilities table
    

    
class Levels():
    pass
        
    
    
    
    
    
    
    
    
