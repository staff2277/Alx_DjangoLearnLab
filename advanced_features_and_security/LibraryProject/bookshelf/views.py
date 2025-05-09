from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from .models import Book
from .forms import BookSearchForm
from .forms import ExampleForm  # Explicit separate import

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  
    form = BookSearchForm(request.GET or None)  # Initialize search form
    
    if form.is_valid():  # Validate form input
        search_query = form.cleaned_data.get("search_query")
        if search_query:
            books = books.filter(Q(title__icontains=search_query) | Q(author__icontains=search_query))

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})
