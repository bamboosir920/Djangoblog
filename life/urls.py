# 引入path
from django.urls import path

# 引入views.py
from . import views

# 正在部署的应用的名称
app_name = 'life'

urlpatterns = [
    # path函数将url映射到视图
    path('life-list/', views.life_list, name='life_list'),
    # 文章详情
    path('life-detail/<int:id>/', views.life_detail, name='life_detail'),
    
]