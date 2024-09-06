from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BooksListCreate.as_view(), name='books'),
    path('books/add', views.add_book, name='add_book'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
