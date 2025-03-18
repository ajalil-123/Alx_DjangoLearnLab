from django.contrib.auth.models import User
from rest_framework import status
from api.models import Book, Author
from api.serializers import BookSerializer
from rest_framework.test import APIClient
from django.test import TestCase

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create an Author instance
        self.author = Author.objects.create(name="John Doe")
        
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a Book instance for testing
        self.book = Book.objects.create(
            title="Test Book", 
            author=self.author, 
            publication_year=2023
        )

        # Define the URL for the book list endpoint
        self.url = '/api/books/'

        # Set up the test client
        self.client = APIClient()

        # Login the client with the test user
        self.client.login(username='testuser', password='password')

    def test_create_book(self):
        # Test the creation of a new book
        book_data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2024
        }
        
        # Make a POST request to create a book
        response = self.client.post(self.url, book_data, format="json")
        
        # Check that the book was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        # Test updating an existing book
        updated_data = {
            "title": "Updated Test Book",
            "author": self.author.id,
            "publication_year": 2025
        }

        # Make a PUT request to update the book
        response = self.client.put(f'{self.url}{self.book.id}/', updated_data, format="json")
        
        # Check that the book was updated successfully
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Test Book")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(f'{self.url}{self.book.id}/')
        
        # Check that the book was deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_unauthenticated_access(self):
        # Test that unauthenticated users cannot access the API
        # Log out the client
        self.client.logout()

        # Make a GET request without authentication
        response = self.client.get(self.url)
        
        # Check that the response is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
