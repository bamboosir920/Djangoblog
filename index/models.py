from django.db import models

# Create your models here.
# timezone 用于处理时间相关事务。
from django.utils import timezone
#路由重定向
from django.urls import reverse
# 记得导入！
from PIL import Image
# 首页信息模型
class SeriesBg(models.Model):
    """
    """
    title = models.CharField(max_length=100,default="bg")
     # 文章标题图
    avatar = models.URLField(default="https://s1.ax1x.com/2022/04/11/LEjUYV.jpg")


    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title