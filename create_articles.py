import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hexlet_django_blog.settings')
django.setup()

from hexlet_django_blog.article.models import Article

# Удаляем старые статьи
Article.objects.all().delete()

# Создаём 20 статей
for i in range(1, 21):
    Article.objects.create(
        name=f"Статья {i}",
        body=f"Содержимое статьи {i}. " + "Много текста для наполнения... " * 10
    )

print(f"Создано {Article.objects.count()} статей")