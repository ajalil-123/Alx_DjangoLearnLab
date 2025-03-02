from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.views.generic import DetailView
from django.shortcuts import render
from .models import Library

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Library

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)





class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # Retrieve all books in the library
        return context