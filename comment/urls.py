from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
     # 项目栏发表评论
    path('post-project-comment/<int:project_id>/', views.post_project_comment, name='post_project_comment'),
    # 项目栏发表评论
    path('post-life-comment/<int:life_id>/', views.post_life_comment, name='post_life_comment'),
]