from django.conf.urls import url
from . import views

urlpatterns = [
    # 書籍
    url(r'bet/(?P<name>[\w-]+)/$', views.mfc,name='mfc_bet'),
    url(r'fight/(?P<name>[\w-]+)/$', views.mfcfight, name='mfc_fight'),
    url(r'playerdata/(?P<name>[\w-]+)/$', views.playerview, name='player_data'),
]