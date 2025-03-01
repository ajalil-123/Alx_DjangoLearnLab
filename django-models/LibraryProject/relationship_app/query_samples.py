
# relationship_app/query_samples.py
# import os
# import django

# # Setup Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject1.settings')
# django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    books = Book.objects.filter(library__name=library_name)
    return books

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    librarian = Librarian.objects.filter(library__name=library_name).first()
    return librarian


