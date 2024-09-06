from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics

from .models import Books
from .serializers import BooksSerializer


class BooksListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksRetieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'pk'

