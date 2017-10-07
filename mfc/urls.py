from django.conf.urls import url
from . import views

urlpatterns = [
    # 書籍
    url(r'(?P<name>[\w-]+)/$', views.mfc,name='user'),   # 削除
]