from django.views import View
from django.http import HttpResponse
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

def index(request, tag, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tag}")