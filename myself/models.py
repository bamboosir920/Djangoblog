from django.db import models

# Create your models here.
# 首页信息模型
class FriendLink(models.Model):
    """
    友链标题
    """
    title = models.CharField(max_length=100,default="Bilibili")
    
    """
    友链名字
    """
    name = models.CharField(max_length=100,blank=True)
    '''
    友链地址
    '''
    url=models.URLField(default="https://space.bilibili.com/490457522")
    '''
    文章标题图
    '''
    avatar = models.URLField(default="https://s1.ax1x.com/2022/04/11/LEjUYV.jpg")


    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title