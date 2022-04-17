from django.shortcuts import render

# 导入数据模型ArticlePost
from .models import ArticlePost
# 引入markdown模块
import markdown
# 引入分页模块
from django.core.paginator import Paginator
# 引入 Q 对象
from django.db.models import Q
# 记得导入！
from PIL import Image
from django.shortcuts import get_object_or_404
from comment.models import Comment
from index.models import SeriesBg

# 文章列表
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')
    
    #背景图
    seriesbg_list = SeriesBg.objects.all()
    seriesbg1=seriesbg_list[0]
    
    # 初始化查询集
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    # 取出所有博客文章
    article_list = ArticlePost.objects.all()

    # 搜索查询集
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''
        
    # 栏目查询集
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)

    # 标签查询集
    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])

    # 查询集排序
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')
        
    # 每页显示 6 篇文章
    paginator = Paginator(article_list, 6)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    
    # 需要传递给模板（templates）的对象
    context = {
        'articles': articles,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
        'seriesbg1':seriesbg1,
    }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    # article = ArticlePost.objects.get(id=id)
    article = get_object_or_404(ArticlePost, id=id)
    # 取出文章评论
    comments = Comment.objects.filter(article=id)
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
    article.body = md.convert(article.body)
    
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    
    # 需要传递给模板的对象
    context = { 'article': article, 'toc': md.toc, 'comments': comments }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

# 404
def page_error(request):
    return render(request, '404.html', status=404)


# 500
def page_not_found(request, exception):
    return render(request, '404.html', status=500)