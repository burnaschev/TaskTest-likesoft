from django.shortcuts import render
from rest_framework import generics

from book.models import Book
from book.serializers import BookSerializer


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    pagination_class = LMSPaginator



class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
