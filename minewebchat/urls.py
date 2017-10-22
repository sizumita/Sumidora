# coding: utf-8
from django.conf.urls import url
from . import views
from django.conf.urls import url, include
from django.contrib import admin
from SQMFC.urls import router as chat_router

urlpatterns = [
    url(r'nowlog/$',views.nowlog,name='nowlog'),
    url(r'^api/', include(chat_router.urls)),
]
