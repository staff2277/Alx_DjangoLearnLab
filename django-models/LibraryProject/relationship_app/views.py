from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Ensure correct template path
    context_object_name = "library"

def list_books(request):
    books = Book.objects.all()  # Changed to use Book.objects.all() as required
    return render(request, "relationship_app/list_books.html", {"books": books})  # Fixed template path
