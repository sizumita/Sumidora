"""SQMFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from minewebchat.views import ChatViewSet
from main.views import mainpage,data

router = routers.DefaultRouter()
router.register(r'chat', ChatViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mfc/', include('mfc.urls', namespace='mfc')),
    url(r'^chat/',include('minewebchat.urls', namespace='chat')),
    url(r'^$',mainpage,name='main'),
    url(r'^data/(?P<name>[\w-]+)/$',data,name='data')
]



