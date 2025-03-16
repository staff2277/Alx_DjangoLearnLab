from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        """Set up test data and test client"""
        self.client = APIClient()
        
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

        self.author = Author.objects.create(name="J.K. Rowling")

        self.book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", 
                                         publication_year=1997, 
                                         author=self.author)

        self.book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", 
                                         publication_year=1998, 
                                         author=self.author)

        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book(self):
        data = {"title": "New Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {"title": "Updated Title", "publication_year": 2025, "author": self.author.id}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author__name": "J.K. Rowling"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Chamber"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Harry Potter and the Chamber of Secrets")

   
    def test_order_books_by_title(self):
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Harry Potter and the Chamber of Secrets")

    def test_unauthenticated_access(self):
        self.client.logout()
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {"title": "Unauthorized Book", "publication_year": 2025, "author": self.author.id}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
