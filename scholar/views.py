from django.shortcuts import render

# 导入数据模型ManuscriptsPost
from .models import ManuscriptsPost
# 引入markdown模块
import markdown
# 引入分页模块
from django.core.paginator import Paginator
# 引入 Q 对象
from django.db.models import Q
# 记得导入！
from PIL import Image
from django.shortcuts import get_object_or_404
from index.models import SeriesBg

# 文章列表
def scholar_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')
    
        #背景图
    seriesbg_list = SeriesBg.objects.all()
    seriesbg3=seriesbg_list[2]
    
    # 初始化查询集
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    # 取出所有博客文章
    scholar_list = ManuscriptsPost.objects.all()

    # 搜索查询集
    if search:
        scholar_list = scholar_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''
        
    # 栏目查询集
    if column is not None and column.isdigit():
        scholar_list = scholar_list.filter(column=column)

    # 标签查询集
    if tag and tag != 'None':
        scholar_list = scholar_list.filter(tags__name__in=[tag])

    # 查询集排序
    if order == 'total_views':
        scholar_list = scholar_list.order_by('-total_views')
        
    # 每页显示 6 篇文章
    paginator = Paginator(scholar_list, 6)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 scholars
    scholars = paginator.get_page(page)
    
    # 需要传递给模板（templates）的对象
    context = {
        'scholars': scholars,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
        'seriesbg3':seriesbg3,
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'scholar/list.html', context)

# 文章详情
def scholar_detail(request, id):
    # 取出相应的文章
    # scholar = scholarPost.objects.get(id=id)
    scholar = get_object_or_404(ManuscriptsPost, id=id)

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
    scholar.body = md.convert(scholar.body)
    
    # 浏览量 +1
    scholar.total_views += 1
    scholar.save(update_fields=['total_views'])
    
    # 需要传递给模板的对象
    context = { 'scholar': scholar, 'toc': md.toc}
    # 载入模板，并返回context对象
    return render(request, 'scholar/detail.html', context)