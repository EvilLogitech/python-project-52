from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

# Create your tests here.
class StatusesTestCase(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_crud(self):
        """testing views for status model"""
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)