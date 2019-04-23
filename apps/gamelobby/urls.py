from django.conf.urls import url
from apps.gamelobby.views import gamelobby,  pvp, pvpNew
#activegame,index

urlpatterns = [
    
    url(r'^$', gamelobby, name='lobby'),
    url(r'^pvp/(?P<room_name>[^/]+)/$', pvp, name='active'),
    #url(r'^gamelobby$', index , name='index'),
    url(r'^pvp/$', pvp , name='pvp'),
    url(r'^pvp/new$', pvpNew , name='pvpnew'),
]