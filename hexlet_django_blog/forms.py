from django import forms
from django.forms import ModelForm
from hexlet_django_blog.article.models import ArticleComment

class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Напишите ваш комментарий..."
            }),
        }
        labels = {
            "content": "",  
        }