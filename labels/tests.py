from django.test import TestCase, Client
from django.urls import reverse
from users.models import TaskManagerUser
from django.utils.translation import gettext as _


class TestLabels(TestCase):

    fixtures = [
        'statuses.json',
        'labels.json',
        'users.json',
        'tasks.json'
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(TaskManagerUser.objects.first())

    def test_labes_crud(self):
        response = self.client.get(reverse('labels'))
        self.assertNotContains(response, 'Third label')

        response = self.client.post(
            reverse('labels_create'), data={'name': 'Third label'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('labels'))

        response = self.client.get(reverse('labels'))
        self.assertContains(response, 'Third label')

        response = self.client.post(
            reverse('labels_update', kwargs={'pk': 4}),
            data={'name': 'Updated'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('labels'))

        response = self.client.get(reverse('labels'))
        self.assertNotContains(response, 'Third label')
        self.assertContains(response, 'Updated')

        response = self.client.post(
            reverse('labels_delete', kwargs={'pk': 4})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('labels'))

        response = self.client.get(reverse('labels'))
        self.assertNotContains(response, 'Updated')

        response = self.client.post(
            reverse('labels_delete', kwargs={'pk': 1})
        )
        response = self.client.get(reverse('labels'))
        self.assertContains(
            response,
            _('Невозможно удалить метку, потому что она используется')
        )
