# 引入path
from django.urls import path

# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'scholar'

urlpatterns = [
    # path函数将url映射到视图
    path('scholar-list/', views.scholar_list, name='scholar_list'),
    # 文章详情
    path('scholar-detail/<int:id>/', views.scholar_detail, name='scholar_detail'),
]