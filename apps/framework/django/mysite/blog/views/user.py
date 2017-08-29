# -*- coding: utf-8 -*-

from django.shortcuts import render
from blog.models import User


def index(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {'users': users})


def detail(request, uid):   # 关于路径变量的使用
    user = User.objects.get(id=uid)  # get 只能返回一个对象，如果结果集为多个对象就会报错
    return render(request, 'user/detail.html', {'user': user})

