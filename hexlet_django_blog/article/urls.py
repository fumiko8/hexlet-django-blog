from django.urls import path
from .views import IndexView
from . import views

app_name = 'article'

urlpatterns = [
    path("tags/<str:tag>/<int:article_id>/", views.index, name = 'article'),
]