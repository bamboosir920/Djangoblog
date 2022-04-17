# 引入path
from django.urls import path

# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'project'

urlpatterns = [
    # path函数将url映射到视图
    path('project-list/', views.project_list, name='project_list'),
    # 文章详情
    path('project-detail/<int:id>/', views.project_detail, name='project_detail'),
    
]