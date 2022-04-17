# Register your models here.
from django.contrib import admin

# 别忘了导入projectrPost
from .models import ProjectPost


# 注册ProjectPost到admin中
admin.site.register(ProjectPost)
