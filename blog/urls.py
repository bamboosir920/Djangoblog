"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from article import views
# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 首页
    path('', include('index.urls', namespace='index')),
    #管理页面
    path('admin/', admin.site.urls),
    # 文章
    path('article/', include('article.urls', namespace='article')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
    # 项目
    path('project/', include('project.urls', namespace='project')),
    # 自己介绍
    path('myself/', include('myself.urls', namespace='myself')),
    # 经历
    path('life/', include('life.urls', namespace='life')),
    # 学术成果
    path('scholar/', include('scholar.urls', namespace='scholar')),
]
#添加这行
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.page_not_found
handler500 = views.page_error