from django.shortcuts import render

# 导入数据模型LifePost
from .models import LifePost
# 引入markdown模块
import markdown
# 引入分页模块
from django.core.paginator import Paginator
# 引入 Q 对象
from django.db.models import Q
# 记得导入！
from PIL import Image
from django.shortcuts import get_object_or_404
from comment.models import LifeComment
from index.models import SeriesBg

# 文章列表
def life_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')
    
    #背景图
    seriesbg_list = SeriesBg.objects.all()
    seriesbg4=seriesbg_list[3]
    
    # 初始化查询集
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    # 取出所有博客文章
    life_list = LifePost.objects.all()

        # 搜索查询集
    if search:
        life_list = life_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''

    # 栏目查询集
    if column is not None and column.isdigit():
        life_list = life_list.filter(column=column)

    # 标签查询集
    if tag and tag != 'None':
        life_list = life_list.filter(tags__name__in=[tag])

    # 查询集排序
    if order == 'total_views':
        life_list = life_list.order_by('-total_views')
        
    # 每页显示 6 篇文章
    paginator = Paginator(life_list, 3)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 lifes
    lifes = paginator.get_page(page)
    
    # 需要传递给模板（templates）的对象
    context = {
        'lifes': lifes,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
        'seriesbg4':seriesbg4,
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'life/list.html', context)

# 文章详情
def life_detail(request, id):
    # 取出相应的文章
    # Life = LifePost.objects.get(id=id)
    life = get_object_or_404(LifePost, id=id)
    # 取出文章评论
    comments = LifeComment.objects.filter(life=id)
    #将markdown语法渲染成html样式
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
         # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
        ],
        safe_mode=True,
        enable_attributes=False
    )
    life.body = md.convert(life.body)
    
    # 浏览量 +1
    life.total_views += 1
    life.save(update_fields=['total_views'])
    
    # 需要传递给模板的对象
    context = { 'life': life, 'toc': md.toc,'comments':comments}
    # 载入模板，并返回context对象
    return render(request, 'life/detail.html', context)