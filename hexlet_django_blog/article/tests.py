from django.test import TestCase
from django.urls import reverse
from .models import Article
from .factories import ArticleFactory

class ArticleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаём статью через фабрику
        cls.article = ArticleFactory()
        # Данные будут сгенерированы автоматически:
        # - name: случайное предложение
        # - body: случайный абзац

    def test_article_page(self):
        url = reverse("article:article", kwargs={
            "tag": "python",
            "article_id": self.article.pk
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Проверяем, что данные из фабрики отображаются
        self.assertContains(response, f"Статья номер {self.article.pk}")
        self.assertContains(response, "Тег python")

class MainPageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = Article.objects.create(name="article1", body="content1")
    
    def test_main_page_redirects_to_article(self):
        main_url = reverse("home")  
        
        target_url = reverse("article:article", kwargs={
            "tag": "python",
            "article_id": self.article.pk
        })
        
        response = self.client.get(main_url)
        
        self.assertRedirects(response, target_url)