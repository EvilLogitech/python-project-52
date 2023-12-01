from django.test import TestCase, Client
from django.urls import reverse


class TestUsers(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = {
            'username': 'TestUser',
            'first_name': 'First',
            'last_name': 'Last',
            'password1': 'Pass123',
            'password2': 'Pass123',
        }

    def test_users_crud(self):
        response = self.client.get(reverse('users'))
        self.assertNotContains(response, 'First Last')

        response = self.client.post(
            reverse('users_create'), data=self.test_user
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('login'))

        response = self.client.get(reverse('users'))
        self.assertContains(response, 'First Last')

        response = self.client.get(reverse('users_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('login'))

        response = self.client.get(reverse('users_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('login'))

        self.client.login(
            username=self.test_user['username'],
            password=self.test_user['password1']
        )
        self.test_user['last_name'] = 'Second'
        response = self.client.post(
            reverse('users_update', kwargs={'pk': 1}), data=self.test_user
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('users'))
        self.assertContains(response, 'First Second')

        response = self.client.post(reverse('users_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('users'))

        response = self.client.get(reverse('users'))
        self.assertNotContains(response, 'First Second')
