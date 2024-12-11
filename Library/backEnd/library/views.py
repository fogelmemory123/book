from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book


class BookListViewApi(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        total = books.count()
        data = {
            "total_books": total,
            "books": [
                {
                    "id": book.id,
                    "title": book.title,
                    "publication_date": book.publication_date,
                    "authors": [f"{author.first_name} {author.last_name}" for author in book.authors.all()],
                    "genre": book.genre.name,
                    "rating": book.rating,
                }
                for book in books
            ],
        }
        return Response(data)
from django.shortcuts import render

# Create your views here.
