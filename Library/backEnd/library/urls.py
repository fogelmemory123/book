from django.urls import path
from .views import  BookListViewApi

urlpatterns = [
    path('api/books/', BookListViewApi.as_view(), name='book_list'),
]