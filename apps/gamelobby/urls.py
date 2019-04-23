from django.conf.urls import url
from apps.gamelobby.views import gamelobby,pvp,pvpNew

urlpatterns = [
    url(r'^$', gamelobby, name='lobby'),
    url(r'^pvp$', pvp, name='pvp'),
    url(r'^pvp/new$', pvpNew, name='pvpNew'),
    
]