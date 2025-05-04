from django.contrib import admin
from borrow.models import Borrow, BorrowRecord

# Register your models here.

@admin.register(Borrow)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','member']
admin.site.register(BorrowRecord)
