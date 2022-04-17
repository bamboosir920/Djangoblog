# Register your models here.
from django.contrib import admin

# 别忘了导入ManuscriptsrPost
from .models import ManuscriptsPost


# 注册ManuscriptsPost到admin中
admin.site.register(ManuscriptsPost)
