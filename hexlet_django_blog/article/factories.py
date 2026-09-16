import factory
from factory.django import DjangoModelFactory
from .models import Article


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    name = factory.Faker("sentence", nb_words=4)
    body = factory.Faker("paragraph", nb_sentences=5)