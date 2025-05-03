from rest_framework import serializers
from book.models import Book, Category, Author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'biography']

class BookSerializer(serializers.ModelSerializer):

    author_details = AuthorSerializer(source='author', read_only=True)
    category_details = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'author', 'category', 'is_available', 'author_details', 'category_details']
        extra_kwargs = {
        'author': {'write_only': True},
        'category': {'write_only': True}
        }
