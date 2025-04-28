from django.urls import path,include
from book.views import BookViewSet

urlpatterns = [
    path('',BookViewSet)
]
