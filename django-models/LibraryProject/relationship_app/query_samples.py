import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  
    except Author.DoesNotExist:
        return "Author not found"

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return "Library not found"

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return "Library not found"
    except Librarian.DoesNotExist:
        return "No librarian assigned"

if __name__ == "__main__":
    print("Books by Author John Doe:", get_books_by_author("John Doe"))
    print("Books in City Library:", get_books_in_library("City Library"))
    print("Librarian of City Library:", get_librarian_for_library("City Library"))
