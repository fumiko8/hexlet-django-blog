from django.views import View

from django.shortcuts import render

class IndexView(View):
    """Главная страница раздела статей"""

    def get(self, request, *args, **kwargs):
        context = {
            'app_name': 'Приложение Статьи',
            'title': 'Главная страница статей',
            'description': 'Добро пожаловать в раздел статей!',
        }
        return render(request, 'articles/index.html', context)
