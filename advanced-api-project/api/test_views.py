from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author
from datetime import datetime


class BookAPITestCase(TestCase):
    """
    Test case for the Book API endpoints.
    """

    def setUp(self):
        """Set up test environment."""
        self.client = APIClient()

        # Create a test user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

        # Create an Author instance
        self.author = Author.objects.create(name="John Doe")

        # Create a test book with the Author instance
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2023)

        # API endpoint URLs
        self.create_url = reverse("book-create")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.id})
        self.list_url = reverse("book-list")


    def test_create_book(self):
        """Test creating a book."""
        book_data = {
            "title": "New Book",
            "author": self.author.id,  # Send the author's ID, not a name
            "publication_year": 2024
        }

        response = self.client.post(self.create_url, book_data, format="json")

        print("Create Book Response:", response.data)  # Debugging output

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "New Book")


    def test_list_books(self):
        """Test retrieving the book list."""
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)  # Only one test book exists

    def test_update_book(self):
        """Test updating a book's details."""
        updated_data = {
            "title": "Updated Book Title",
            "author": "John Doe",
            "publication_year": 2025
        }

        response = self.client.put(self.detail_url, updated_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")

    def test_delete_book(self):
        """Test deleting a book."""
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure book is deleted

    def test_filter_books(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url, {"title": "Test Book"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access the API."""
        self.client.logout()  # Remove authentication
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
