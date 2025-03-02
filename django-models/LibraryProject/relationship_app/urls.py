
from django.urls import path
from .views import book_list,LibraryDetailView

urlpatterns = [
    path('', view=book_list, name='books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]



