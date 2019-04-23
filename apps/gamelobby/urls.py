from django.conf.urls import url
from apps.gamelobby.views import gamelobby, index, activegame, pvp, pvpnew

urlpatterns = [
    
    url(r'^$', gamelobby, name='lobby'),
    url(r'^(?P<room_name>[^/]+)/$', activegame, name='active'),
    url(r'^gamelobby$', index , name='index'),
    url(r'^pvp/$', pvp , name='pvp'),
    url(r'^pvp/new$', pvpnew , name='pvpnew'),
]