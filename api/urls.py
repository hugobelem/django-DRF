from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BooksListCreate.as_view(), name='books'),
    path('books/<int:pk>/',
         views.BooksRetieveUpdateDestroy.as_view(),
         name='update'),
    path('books/filter/', views.BooksAuthor.as_view(), name='filter')
]
