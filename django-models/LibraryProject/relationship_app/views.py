from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book



class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"


def list_books(request):
    books = Book.objects.select_related("author").all() 
    return render(request, "list_books.html", {"books": books})

