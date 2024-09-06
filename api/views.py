from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from .models import Books
from .serializers import BooksSerializer


class BooksListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksRetieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    lookup_field = 'pk'

class BooksAuthor(APIView):
    def get(self, request, format=None):
        author = request.query_params.get('author', '')

        if author:
            book = Books.objects.filter(author__icontains=author)
        else:
            book = Books.objects.all()

        serializer = BooksSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)