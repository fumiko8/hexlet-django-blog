from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse
from hexlet_django_blog.article.models import Article


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


def home_redirect(request):
    # Редирект на первую статью в БД
    first_article = Article.objects.first()
    if first_article:
        url = reverse('article:article', kwargs={
            'tag': 'python',
            'article_id': first_article.pk
        })
    else:
        url = reverse('about')
    return redirect(url)
