from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # Ensure Book is imported

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Keep path explicit
    context_object_name = "library"

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Ensuring "Book.objects.all()" is explicitly present
    return render(request, "relationship_app/list_books.html", {"books": books})  # Using correct template path
