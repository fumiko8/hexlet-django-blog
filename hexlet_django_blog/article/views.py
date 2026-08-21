from django.shortcuts import render

def index(request):
    context = {
        'app_name': 'Приложение Статьи',
        'title': 'Главная страница статей',
        'description': 'Добро пожаловать в раздел статей!',
    }
    return render(request, 'articles/index.html', context)