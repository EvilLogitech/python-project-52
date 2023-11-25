from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestUsers(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_user(self):
        user = User(username="TestUser", first_name="First", last_name="Last")
        user.set_password('12345')
        user.save()
        response = self.client.get(reverse('users'))
        self.assertContains(response, "TestUser")
        self.assertContains(response, "First Last")
