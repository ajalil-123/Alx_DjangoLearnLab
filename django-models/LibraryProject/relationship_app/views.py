from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


from django.views.generic import DetailView
from django.shortcuts import render
from .models import Library


def book_list(request):
    books = Book.objects.all()  # Retrieve all books
    book_details = "\n".join([f"{book.title} - {book.author.name}" for book in books])  # Format output
    return HttpResponse(f"List of Books:\n{book_details}", content_type="text/plain")




from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # Retrieve all books in the library
        return context