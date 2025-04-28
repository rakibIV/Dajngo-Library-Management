from django.db import models
from users.models import User
from book.models import Book
from uuid import uuid4
# Create your models here.

class Borrow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    member = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Borrow record of {self.member.first_name}"
    
class BorrowRecord(models.Model):
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE, related_name='borrow')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    borrowed_date = models.DateField(auto_now_add=True)
    borrow_status = models.BooleanField(default=False)
    return_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = [['borrow', 'book']]
        
    def __str__(self):
        return f"{self.book.title} borrowed on {self.borrowed_date}"
