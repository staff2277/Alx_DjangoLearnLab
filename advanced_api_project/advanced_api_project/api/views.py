from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """View to retrieve a list of all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """View to retrieve a single book by its ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """View to add a new book (only accessible to authenticated users)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """View to update an existing book (only accessible to authenticated users)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """View to delete a book (only accessible to authenticated users)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
