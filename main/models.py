from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.title
