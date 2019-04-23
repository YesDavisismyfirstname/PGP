from django.conf.urls import include, url
from apps.login.views import user_list,log_in, log_out, sign_up, landing
from apps.game_window.views import gamewindow

urlpatterns = [
    url(r'^$', gamewindow, name='lobby'),
]