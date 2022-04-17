# Create your models here.
from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
#路由重定向
from django.urls import reverse
# Django-taggit
from taggit.managers import TaggableManager
# 记得导入！
from PIL import Image
    
class LifePost(models.Model):
    '''
    经历信息
    '''
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100)
    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
    #阅读量
    total_views = models.PositiveIntegerField(default=0)
    
    '''
    经历记录
    '''
    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()

    '''
    经历标签
    '''
    # 文章标签
    tags = TaggableManager(blank=True)

    '''
    经历展示图
    '''
    # 文章标题图
    # 原来为本地图片，在v0.6以后改为网络存储
    # avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    avatar = models.URLField(default="https://s1.ax1x.com/2022/04/11/LEjUYV.jpg")
    #  # 保存时处理图片
    # def save(self, *args, **kwargs):
    #     # 调用原有的 save() 的功能
    #     Life = super(LifePost, self).save(*args, **kwargs)

    #     # 固定宽度缩放图片大小
    #     if self.avatar and not kwargs.get('update_fields'):
    #         image = Image.open(self.avatar)
    #         (x, y) = image.size
    #         new_x = 400
    #         new_y = int(new_x * (y / x))
    #         resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
    #         resized_image.save(self.avatar.path)
    # return Life
        
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
    
    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
    # 获取文章地址
    def get_absolute_url(self):
        return reverse('life:life_detail', args=[self.id])