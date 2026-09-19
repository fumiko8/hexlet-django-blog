from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, DetailView

from hexlet_django_blog.forms import ArticleCommentForm
from .models import Article


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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            return redirect('article:articles_show', pk=self.object.pk)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)