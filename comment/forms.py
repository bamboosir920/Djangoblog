from django import forms
from .models import Comment,ProjectComment,LifeComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = ProjectComment
        fields = ['body']

class LifeCommentForm(forms.ModelForm):
    class Meta:
        model = LifeComment
        fields = ['body']