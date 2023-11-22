from rest_framework import generics

from book.models import Book
from book.paginators import BookPaginator
from book.serializers import BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    """Создание книги"""
    serializer_class = BookSerializer


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListAPIView(generics.ListAPIView):
    """Просмотр списка книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = BookPaginator


class BookUpdateAPIView(generics.UpdateAPIView):
    """Редактирование книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDestroyAPIView(generics.DestroyAPIView):
    """Удаление книги"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
