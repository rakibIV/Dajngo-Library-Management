from django.db import models
import random

# Create your models here.

def generate_unique_isbn():
    from .models import Book
    while True:
        isbn = ''.join(str(random.randint(0, 9)) for _ in range(13))
        if not Book.objects.filter(isbn=isbn).exists():
            return isbn

class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13, unique=True, default=generate_unique_isbn)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
    

