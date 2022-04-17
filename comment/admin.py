from django.contrib import admin



from .models import Comment
from .models import LifeComment
from .models import ProjectComment

# 注册ArticlePost到admin中
admin.site.register(Comment)

# 注册ArticlePost到admin中
admin.site.register(LifeComment)
# 注册文章栏目
admin.site.register(ProjectComment)
# Register your models here.
