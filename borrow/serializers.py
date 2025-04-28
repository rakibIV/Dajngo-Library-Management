from rest_framework import serializers
from borrow.models import Borrow, BorrowRecord
from book.models import Book
from django.utils import timezone


class BorrowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['id','member','created_at']
        
        
        
class BorrowRecordSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    class Meta:
        model = BorrowRecord
        fields = ['id','borrow','book','borrowed_date','borrow_status','return_date']
        
        
        
class CreateBorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book']
        

    
        
    def validate_book(self, book):
        borrow = self.context.get('borrow')
        
        if borrow is None:
            raise serializers.ValidationError("Borrow instance is missing.")

        if not book.is_available:
            raise serializers.ValidationError("This book is not available for borrowing.")

        if BorrowRecord.objects.filter(borrow=borrow, book=book).exists():
            raise serializers.ValidationError(
                f"This book is already in your borrow list. If you want to borrow it again, update your previous record."
            )
        return book
        
        
    def create(self, validated_data):
        borrow_id = self.context['borrow_id']
        borrow = Borrow.objects.get(id = borrow_id)
        borrow_record = BorrowRecord.objects.create(borrow = borrow,borrow_status=True, **validated_data)
        borrow_record.book.is_available = False
        borrow_record.book.save()
        return borrow_record
        
        
        
        
class UpdateBorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['borrow_status']
        
        
    def update(self, instance, validated_data):
        previous_status = instance.borrow_status
        new_status = validated_data.get('borrow_status')
        
        if previous_status != new_status:
            if new_status == False:
                instance.return_date = timezone.now().date()
                instance.book.is_available = True
                instance.book.save()
                
            elif new_status == True:
                if not instance.book.is_available:
                    raise serializers.ValidationError("This book has already been borrowed by someone else.")
                
                instance.return_date = None
                instance.book.is_available = False
                instance.book.save()
                
            instance.borrow_status = new_status
            instance.save()
            return instance
        
        return instance
    

