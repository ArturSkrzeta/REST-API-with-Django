from django.db import models

class User(models.Model):
    email = models.CharField(max_length=30, default='', unique=True)
    nick = models.CharField(max_length=20, default='', unique=True)
    level = models.IntegerField(null=False, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
