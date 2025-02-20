from .models import Book, Library, Librarian

def get_books_by_author(author):
    return Book.objects.filter(author=author)

def get_books_in_library(library):
    return library.books.all()

def get_librarian_for_library(library):
    return Librarian.objects.get(library=library)