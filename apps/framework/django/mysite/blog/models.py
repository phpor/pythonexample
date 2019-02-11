# encoding=utf-8
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Feed(models.Model):

    fid = models.BigAutoField(primary_key=True)
    ctime = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.content
