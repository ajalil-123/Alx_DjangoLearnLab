from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

from django.views.generic.detail import DetailView
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




#from django.contrib.auth.models import User

# Create a new user
#user = User.objects.create_user('john', 'john@example.com', 'password123')

# Retrieve a user based on username
#user = User.objects.get(username='john')



from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import render, redirect


class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user automatically after registration
            return redirect("login")
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/registration.html", {"form": form})
