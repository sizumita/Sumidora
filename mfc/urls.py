from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bet/(?P<name>[\w-]+)/$', views.mfc,name='bet'),
    url(r'fight/(?P<name>[\w-]+)/$', views.mfcfight, name='fight'),
    url(r'playerdata/(?P<name>[\w-]+)/$', views.playerview, name='player_data'),
    url(r'fightdata/(?P<number>[\w-]+)/$', views.fightdata, name='fight_data'),

]