# Register your models here.
from django.contrib import admin

from .models import FriendLink

# 注册FriendLink到admin中
admin.site.register(FriendLink)
