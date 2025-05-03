from rest_framework import serializers
from borrow.models import Borrow, BorrowRecord
from book.models import Book
from django.utils import timezone
from borrow.services import BorrowRecordServices



class BorrowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['id','member','created_at']
        read_only_fields = ['member']
        
    def validate(self, attrs):
        user = self.context['request'].user
        borrow = Borrow.objects.filter(member=user).exists()
        
        if borrow:
            raise serializers.ValidationError("You already have a borrow record. go through with the borrow id")
        
        borrow = Borrow.objects.create(member=user)
        
        return borrow
        
        
        
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
        BorrowRecordServices.validate_book_for_borrowing(borrow,book)
        return book
        
        
    def create(self, validated_data):
        borrow_id = self.context.get('borrow_id')
        return BorrowRecordServices.create_borrow_record(borrow_id, validated_data.get('book'))
        
        
        
        
class UpdateBorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['borrow_status']
        
        
    def update(self, instance, validated_data):
        return BorrowRecordServices.update_borrow_record(instance, validated_data.get('borrow_status'))
    

