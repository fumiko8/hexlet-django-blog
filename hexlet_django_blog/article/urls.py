from django.urls import path
from .views import IndexView, ArticleListView, ArticleDetailView, index
from . import views

app_name = 'article'

urlpatterns = [
    path("", ArticleListView.as_view(), name='list'),
    path("<int:pk>/", ArticleDetailView.as_view(), name = 'articles_show'),
]