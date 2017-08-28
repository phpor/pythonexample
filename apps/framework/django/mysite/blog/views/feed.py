# -*- coding: utf-8 -*-

from django.shortcuts import render
from blog.models import Feed


def index(request):
    feeds = Feed.objects.all()
    return render(request, 'feed/list.html', {'feeds': feeds})


def detail(request, fid):   # 关于路径变量的使用
    feed = Feed.objects.get(fid=fid)
    return render(request, 'feed/detail.html', {'feed': feed})

