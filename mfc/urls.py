from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bet/(?P<name>[\w-]+)/(?P<page>[\w-]+)/$', views.mfc,name='mfc_bet'),
    url(r'fight/(?P<name>[\w-]+)/$', views.mfcfight, name='mfc_fight'),
    url(r'playerdata/(?P<name>[\w-]+)/$', views.playerview, name='player_data'),
    url(r'fightdata/(?P<name>[\w-]+)/$', views.fightdata, name='fight_data'),
    url(r'eroor$', views.fightdata, name='EROOR'),

]