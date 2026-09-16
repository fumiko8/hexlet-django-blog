from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import ListView, DetailView


class IndexView(View):
    """Главная страница раздела статей"""

    def get(self, request, *args, **kwargs):
        context = {
            'app_name': 'Приложение Статьи',
            'title': 'Главная страница статей',
            'description': 'Добро пожаловать в раздел статей!',
        }
        return render(request, 'articles/index.html', context)

class ArticleListView(ListView):
    model = Article
    paginate_by = 15
    template_name = 'article/article_list.html'
    context_object_name = 'articles'

def index(request, tag, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tag}")

class ArticleDetailView(DetailView):
    model = Article

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article/article_detail.html', {'article': article})