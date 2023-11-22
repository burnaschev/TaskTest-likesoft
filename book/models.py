from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    author = models.CharField(max_length=60, verbose_name='автор')
    year_publication = models.DateField(verbose_name='год издания')
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
