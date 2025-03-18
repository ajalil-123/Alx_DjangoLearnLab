from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


#implement generic views for to handle CRRUD operations

#Generic view that list all books 
class ListView(generics.ListAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer



#Generic view that provides details of all books 
class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

#Generic view that creates new books 
class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


