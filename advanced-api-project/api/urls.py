from django.urls import path

from .views import ListView, CreateView, UpdateView, DeleteView, DetailView


urlpatterns = [
    path("books/", ListView.as_view(), name= 'book-list'),
    path("books/detail/<int:pk>/", DetailView.as_view(), name= 'book-detail'),
    path("books/create", CreateView.as_view(), name= 'book-create'),
    path("books/update/<int:pk>/", UpdateView.as_view(), name= 'book-update'),
    path("books/destroy/<int:pk>/", DeleteView.as_view(), name= 'book-destroy')
]