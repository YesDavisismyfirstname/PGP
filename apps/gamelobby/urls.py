from django.conf.urls import url
from apps.gamelobby.views import gamelobby

urlpatterns = [
    url(r'^$', gamelobby, name='lobby'),
]