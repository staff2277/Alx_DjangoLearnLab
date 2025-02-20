import django
import os

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Update with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # ✅ Fix: Using objects.filter()
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
        return Librarian.objects.get(library=library)  # ✅ Fix: Using objects.get(library=library)
    except Library.DoesNotExist:
        return "Library not found"
    except Librarian.DoesNotExist:
        return "No librarian assigned"

if __name__ == "__main__":
    print("Books by Author John Doe:", get_books_by_author("John Doe"))
    print("Books in City Library:", get_books_in_library("City Library"))
    print("Librarian of City Library:", get_librarian_for_library("City Library"))
