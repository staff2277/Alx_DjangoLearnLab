from django.shortcuts import get_object_or_404
from rest_framework import generics, filters  # ✅ Ensure filters is imported
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend  # ✅ Ensure this is imported
from rest_framework.filters import OrderingFilter  # ✅ Explicit import

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]  # ✅ Explicitly adding OrderingFilter
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
