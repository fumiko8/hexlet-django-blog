from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    body = models.TextField(verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleComment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True,           # ← разрешаем NULL в БД
        blank=True,          # ← разрешаем пустое значение в форме
    )
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    TRAINEE = 'TR'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CEO = 'CEO'

    POSITIONS = [
        (TRAINEE, 'Trainee'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (CEO, 'CEO'),
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=3, choices=POSITIONS, default=TRAINEE)

    def __str__(self):
        return self.name