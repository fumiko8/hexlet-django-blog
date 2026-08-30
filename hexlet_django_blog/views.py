from django.views.generic import TemplateView

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