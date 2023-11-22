from django.urls import path

from book.apps import BookConfig
from book.views import BookCreateAPIView, BookRetrieveAPIView, BookListAPIView, BookDestroyAPIView, BookUpdateAPIView

app_name = BookConfig.name

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('update/<int:pk>/', BookUpdateAPIView.as_view(), name='book_update'),
    path('view/<int:pk>/', BookRetrieveAPIView.as_view(), name='book_view'),
    path('delete/<int:pk>/', BookDestroyAPIView.as_view(), name='book_delete'),

]
