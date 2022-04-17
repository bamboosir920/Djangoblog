# Register your models here.
from django.contrib import admin

# 别忘了导入LiferPost
from .models import LifePost


# 注册LifePost到admin中
admin.site.register(LifePost)
