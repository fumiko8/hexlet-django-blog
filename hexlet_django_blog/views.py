from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import redirect


class IndexView(TemplateView):
    """Главная страница"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

class AboutView(TemplateView):
    """Страница 'О нас' """
    template_name = 'about.html'

def home_redirect(request):
    url = reverse('article:article', kwargs={'tag': 'python', 'article_id': 42})
    return redirect(url)