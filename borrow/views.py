from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from borrow.models import Borrow, BorrowRecord
from borrow.serializers import BorrowSerializers, BorrowRecordSerializer, CreateBorrowRecordSerializer, UpdateBorrowRecordSerializer


# Create your views here.


class BorrowViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializers
    


class BorrowRecordViewSet(ModelViewSet):
    
    def get_queryset(self):
        return BorrowRecord.objects.filter(borrow_id=self.kwargs['borrow_pk'])
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateBorrowRecordSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateBorrowRecordSerializer

        return BorrowRecordSerializer
    
    def get_serializer_context(self):
        borrow = Borrow.objects.get(id=self.kwargs['borrow_pk'])
        return {'borrow': borrow}
        
    

    
