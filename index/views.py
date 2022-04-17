from django.shortcuts import render

# 记得导入！
from PIL import Image
from django.shortcuts import get_object_or_404
from comment.models import Comment
from .models import SeriesBg

# 文章列表
def index(request):
    seriesbg_list = SeriesBg.objects.all()
    seriesbg1=seriesbg_list[0]
    seriesbg2=seriesbg_list[1]
    seriesbg3=seriesbg_list[2]
    seriesbg4=seriesbg_list[3]
    seriesbg5=seriesbg_list[4]  
    context={
        'seriesbg1':seriesbg1,
        'seriesbg2':seriesbg2,
        'seriesbg3':seriesbg3,
        'seriesbg4':seriesbg4,
        'seriesbg5':seriesbg5,
    }
    return render(request, 'index/index.html',context)