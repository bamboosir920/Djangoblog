from django.db import models
from django.contrib.auth.models import User
from article.models import ArticlePost
from project.models import ProjectPost
from life.models import LifePost

# 博文的评论
class Comment(models.Model):
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
    
# 博文的评论
class ProjectComment(models.Model):
    project = models.ForeignKey(
        ProjectPost,
        on_delete=models.CASCADE,
        related_name='projectcomments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='projectcomments'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
    
# 博文的评论
class LifeComment(models.Model):
    life = models.ForeignKey(
        LifePost,
        on_delete=models.CASCADE,
        related_name='LifeComments'
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='LifeComments'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]