from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    author = models.CharField(max_length=60, verbose_name='автор')
    year_publication = models.PositiveIntegerField(**NULLABLE, verbose_name='год издания')
    isbn = models.CharField(max_length=50, unique=True, verbose_name='isbn')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
