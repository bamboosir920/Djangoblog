# Django搭建的个人博客
## 地址
github:[Django-MyBlog](https://github.com/bamboosir920/Django-MyBlog)

gitee:[Django-MyBlog](https://gitee.com/bamboosir920/django-myblog)

希望可以的话，点一个star~
## 使用指南
使用django3搭建的博客网站
### 关于环境
```python
pip install -r requirements.txt
```
#### 启动项目
```python
python manage.py runserver
```
### 关于后台
一般需要先创造一个admin账户，创建指令在下面，才能进入后台

```python
python manage.py createsuperuser
```

然后上传文件通过后台，后台地址： `127.0.0.1:8000\admin`
### 关于背景
背景图片可以通过后台进行更改:INDEX\Series bgs中进行更改，通过更改图床进行更改背景图片。其中1,2,3,4,5分别为五个项目的背景图。

里面还有一些被注释掉的小功能，暂时没空添加，看以后有机会添加吧
### 关于文章
选择markdown进行记录，可以在后台上传解决。
为了美观考虑，每个文章都添加了一个图片链接，可以通过图传进行保存图片(考虑到本地会存在带宽不够的问题)。
## 基础指令

### 创建项目

```python
django-admin startproject blog
```

### 创建app

```python
python manage.py startapp article
```

### 数据迁移

```python
python manage.py makemigrations

python manage.py migrate
```
# Git同步

添加当前所有更新

```
git add .
```

提交所有更新

```
 git commit -m "-m后这段只是一个提交说明，可以是任何内容"
```

推送仓库

```
git push -u origin master
```

更新仓库

```
git pull --rebase origin master
```
## 展示
### 主页
<img src="https://img-blog.csdnimg.cn/cc652da6b2254c2fa565f8928ecdb758.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">

<img src="https://img-blog.csdnimg.cn/07a3e4db19764edfb12ce6ed28949a4e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">
### 分区页
<img src="https://img-blog.csdnimg.cn/edea52b106484340ae64a242800f53c3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">

<img src="https://img-blog.csdnimg.cn/fc77bab8b656424a9897c23f64c68bbb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">

<img src="https://img-blog.csdnimg.cn/a6365cfecb934c59a0a81d3bf5e13361.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">

<img src="https://img-blog.csdnimg.cn/0387fe5b0b604ccf9fb0dae01e8e24a3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">
<img src="https://img-blog.csdnimg.cn/dfeef04ea3e84691a0e4b5ef14018d10.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">

<img src="https://img-blog.csdnimg.cn/cc0d9655c77f49e8a1adb152f4c168b6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">
<img src="https://img-blog.csdnimg.cn/1c669d598b6746e2a51ce192e582c210.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">

<img src="https://img-blog.csdnimg.cn/d333f19af23d4b3b82b6a119bdac36d1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_20,color_FFFFFF,t_70,g_se,x_16" width="80%">
### 自适应
基本完成了自适应

![在这里插入图片描述](https://img-blog.csdnimg.cn/2e60307fbceb41aa9eba4e4c9b7ec77f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_12,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://img-blog.csdnimg.cn/d0e6076522a04709bd10f6e5933a53ff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_12,color_FFFFFF,t_70,g_se,x_16)

![在这里插入图片描述](https://img-blog.csdnimg.cn/420298e74f0b4b18919344b0b8eed275.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_12,color_FFFFFF,t_70,g_se,x_16)


![在这里插入图片描述](https://img-blog.csdnimg.cn/3b7c68145ebb4cbf834464b5d9d1891a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_12,color_FFFFFF,t_70,g_se,x_16)


![在这里插入图片描述](https://img-blog.csdnimg.cn/d1f1527952be431d95ba958d65a32752.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_13,color_FFFFFF,t_70,g_se,x_16)



![在这里插入图片描述](https://img-blog.csdnimg.cn/287305fad8a14e5daa0a8d7d0e8b81fd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LqM5Lik6YWl6IKJ,size_12,color_FFFFFF,t_70,g_se,x_16)




