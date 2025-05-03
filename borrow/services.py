from django.utils import timezone
from borrow.models import Borrow, BorrowRecord
from book.models import Book
from rest_framework.exceptions import ValidationError

class BorrowRecordServices:

    @staticmethod
    def validate_book_for_borrowing(borrow, book):
        if borrow is None:
            raise ValidationError("Borrow instance is missing.")

        if not book.is_available:
            raise ValidationError("This book is not available for borrowing.")

        if BorrowRecord.objects.filter(borrow=borrow, book=book).exists():
            raise ValidationError(
                f"This book is already in your borrow list. If you want to borrow it again, update your previous record."
            )

    @staticmethod
    def create_borrow_record(borrow_id, book):
        borrow = Borrow.objects.get(id=borrow_id)

        BorrowRecordServices.validate_book_for_borrowing(borrow, book)

        borrow_record = BorrowRecord.objects.create(borrow=borrow, borrow_status=True, book=book)
        borrow_record.book.is_available = False
        borrow_record.book.save()
        
        return borrow_record

    @staticmethod
    def update_borrow_record(instance, new_status):
        if instance.borrow_status != new_status:
            if not new_status and instance.return_date is None: 
                instance.return_date = timezone.now().date()
                instance.book.is_available = True
                instance.book.save()
            elif new_status: 
                if not instance.book.is_available:
                    raise ValidationError("This book has already been borrowed by someone else.")

                instance.return_date = None
                instance.book.is_available = False
                instance.book.save()

            instance.borrow_status = new_status
            instance.save()

        return instance
