from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet, CategoryViewSet, AuthorViewSet
from borrow.views import BorrowViewSet, BorrowRecordViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('categories', CategoryViewSet, basename='category')
router.register('authors', AuthorViewSet, basename='author')
router.register('borrows',BorrowViewSet, basename='borrows')

borrow_router = routers.NestedDefaultRouter(router,'borrows', lookup='borrow')
borrow_router.register('records',BorrowRecordViewSet, basename='borrow-records')

urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('',include(borrow_router.urls))
]