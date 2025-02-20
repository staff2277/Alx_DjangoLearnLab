from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView  # Explicit import for Q2
from django.contrib.auth import login  # Explicit import for Q3
from django.contrib.auth.forms import UserCreationForm  # Explicit import for Q3
from .models import Library, Book  # Ensure models are imported
from django.http import HttpResponse

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("list_books")  # Redirect to book listing
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
