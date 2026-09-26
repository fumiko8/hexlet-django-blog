from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path("create/", ArticleCreateView.as_view(), name="articles_create"),
    path('<int:pk>/', ArticleDetailView.as_view(), name='articles_show'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='articles_update'),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="articles_delete"),
]