# 引入path
from django.urls import path

# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'myself'

urlpatterns = [
    # path函数将url映射到视图
    path('', views.myself, name='myself'),
]