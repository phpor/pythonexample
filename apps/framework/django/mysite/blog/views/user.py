# -*- coding: utf-8 -*-

from django.shortcuts import render
from blog.models import User


def index(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {'users': users})


def detail(request, uid):   # 关于路径变量的使用
    user = User.objects.get(id=uid)
    return render(request, 'user/detail.html', {'user': user})

