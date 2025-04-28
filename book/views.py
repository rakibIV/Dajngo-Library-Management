from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from book.models import Book, Category, Author
from book.serializers import BookSerializer, AuthorSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from book.filters import BookFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class BookViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = BookFilter
    pagination_class = PageNumberPagination
    search_fields = ['title']
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
    
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
