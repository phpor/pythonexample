# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from blog.views import feed,user

# 这个变量名的规定的
urlpatterns = [
   # url(r'^$', views.index, name='index'),
    url(r'^user/$', user.index, name='user-list'),
    url(r'^user/(?P<uid>\d+)$', user.detail, name='user-detail'),
    url(r'^feed/$', feed.index, name='feed-list'),
    url(r'^feed/(?P<fid>\d+)$', feed.detail, name='feed-detail'),
]
