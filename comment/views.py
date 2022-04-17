from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import ArticlePost
from project.models import ProjectPost
from life.models import LifePost
from .forms import CommentForm,LifeCommentForm,ProjectCommentForm

# 文章评论
@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")
    
# 文章评论
@login_required(login_url='/userprofile/login/')
def post_project_comment(request, project_id):
    project = get_object_or_404(ProjectPost, id=project_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = ProjectCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.project = project
            new_comment.user = request.user
            new_comment.save()
            return redirect(project)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")
    
# 文章评论
@login_required(login_url='/userprofile/login/')
def post_life_comment(request, life_id):
    life = get_object_or_404(LifePost, id=life_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = LifeCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.life = life
            new_comment.user = request.user
            new_comment.save()
            return redirect(life)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")