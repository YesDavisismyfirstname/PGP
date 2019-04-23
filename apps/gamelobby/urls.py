from django.conf.urls import url
from apps.gamelobby.views import gamelobby, index

urlpatterns = [
    url(r'^$', gamelobby, name='lobby'),
    url(r'^gamelobby$', index , name='index'),
]