from django.shortcuts import render

# 记得导入！
from PIL import Image
from django.shortcuts import get_object_or_404
# 导入数据模型LifePost
from .models import FriendLink
from django.shortcuts import get_object_or_404
from index.models import SeriesBg

# 文章列表
def myself(request):
    #背景图
    seriesbg_list = SeriesBg.objects.all()
    seriesbg5=seriesbg_list[4]
    
    friendlinks = FriendLink.objects.all()
    
    # 需要传递给模板（templates）的对象
    context = {
        'friendlinks': friendlinks,
        'seriesbg5':seriesbg5,
    }
    
     # render函数：载入模板，并返回context对象
    return render(request, 'myself/myself.html', context)