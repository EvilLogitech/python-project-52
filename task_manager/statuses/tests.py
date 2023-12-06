from django.test import TestCase, Client
from django.urls import reverse
from django.utils.translation import gettext as _
from task_manager.users.models import TaskManagerUser


class TestStatuses(TestCase):

    fixtures = [
        'statuses.json',
        'labels.json',
        'users.json',
        'tasks.json'
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(TaskManagerUser.objects.first())

    def test_statuses_crud(self):
        response = self.client.get(reverse('statuses'))
        self.assertNotContains(response, 'Third status')

        response = self.client.post(
            reverse('statuses_create'), data={'name': 'Third status'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('statuses'))

        response = self.client.get(reverse('statuses'))
        self.assertContains(response, 'Third status')

        response = self.client.post(
            reverse('statuses_update', kwargs={'pk': 4}),
            data={'name': 'Updated'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('statuses'))

        response = self.client.get(reverse('statuses'))
        self.assertNotContains(response, 'Third status')
        self.assertContains(response, 'Updated')

        response = self.client.post(
            reverse('statuses_delete', kwargs={'pk': 4})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('statuses'))

        response = self.client.get(reverse('statuses'))
        self.assertNotContains(response, 'Updated')

        response = self.client.post(
            reverse('statuses_delete', kwargs={'pk': 1})
        )
        response = self.client.get(reverse('statuses'))
        self.assertContains(
            response,
            _('Невозможно удалить статус, потому что он используется')
        )
