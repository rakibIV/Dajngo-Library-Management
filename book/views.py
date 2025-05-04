from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from book.models import Book, Category, Author
from book.serializers import BookSerializer, AuthorSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from book.filters import BookFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

# Create your views here.



class BookViewSet(ModelViewSet):
    """
    API endpoint for managing books.
    - Supports searching and pagination.
    - Requires authentication.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve all books",
        operation_description="Returns a paginated list of books. Users can search by title.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a single book",
        operation_description="Fetch details of a specific book using its ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new book",
        operation_description="Allows an admin to add a new book to the collection.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a book",
        operation_description="Modify details of an existing book. Only admins can update.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a book",
        operation_description="Removes a book from the collection. Only admins can delete.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
    
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = BookFilter
    pagination_class = PageNumberPagination
    search_fields = ['title']
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class AuthorViewSet(ModelViewSet):
    """
    API endpoint for managing authors.
    - Requires admin privileges.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve all authors",
        operation_description="Returns a list of all authors.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an author",
        operation_description="Fetch details of a specific author using their ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new author",
        operation_description="Allows an admin to add a new author.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an author",
        operation_description="Modify details of an existing author. Only admins can update.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an author",
        operation_description="Removes an author from the system. Only admins can delete.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]
    
    
class CategoryViewSet(ModelViewSet):
    """
    API endpoint for managing book categories.
    - Requires admin privileges.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve all categories",
        operation_description="Returns a list of all book categories.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a category",
        operation_description="Fetch details of a specific category using its ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new category",
        operation_description="Allows an admin to add a new book category.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a category",
        operation_description="Modify details of an existing category. Only admins can update.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a category",
        operation_description="Removes a category from the system. Only admins can delete.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
