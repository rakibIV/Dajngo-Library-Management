from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from borrow.models import Borrow, BorrowRecord
from borrow.serializers import BorrowSerializers, BorrowRecordSerializer, CreateBorrowRecordSerializer, UpdateBorrowRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


class BorrowViewSet(ModelViewSet):
    """
    API endpoint for borrowing books.
    - Users can only manage their own borrow records.
    - Requires authentication.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve the current user's borrow",
        operation_description="Returns the borrow for the authenticated user.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a borrow",
        operation_description="Fetch details of a specific borrow.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new borrow",
        operation_description="Allows an authenticated user to keep a borrow record under the created borrow model.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    
    permission_classes = [IsAuthenticated]
    serializer_class = BorrowSerializers
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Borrow.objects.none()
        return Borrow.objects.filter(member=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
    


class BorrowRecordViewSet(ModelViewSet):
    """
    API endpoint for managing borrow records within a borrow transaction.
    - Requires authentication.
    """
    @swagger_auto_schema(
        operation_summary="Retrieve all borrow records for a borrow transaction",
        operation_description="Returns a list of borrow record under a specific borrow.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a borrow record",
        operation_description="Fetch details of a specific borrow record.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new borrow record",
        operation_description="Allows an authenticated user to borrow a new book creating a new borrow record.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a borrow record",
        operation_description="Modifies a borrow record, such as marking a book as returned.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    
    
    
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['book__title']
    
    def get_queryset(self):
        return BorrowRecord.objects.filter(borrow_id=self.kwargs.get('borrow_pk'))
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateBorrowRecordSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return UpdateBorrowRecordSerializer

        return BorrowRecordSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        if getattr(self, 'swagger_fake_view', False):
            return context
        borrow = Borrow.objects.get(id=self.kwargs.get('borrow_pk'))
        return {'borrow': borrow,'borrow_id': borrow.id}
        
    

    
