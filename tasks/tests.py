from django.test import TestCase, Client
from django.urls import reverse
from users.models import TaskManagerUser
from django.utils.translation import gettext as _


class TestTasks(TestCase):

    fixtures = [
        'statuses.json',
        'labels.json',
        'users.json',
        'tasks.json'
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(TaskManagerUser.objects.first())

    def test_task_crud(self):
        response = self.client.get(reverse('tasks'))
        self.assertContains(response, 'Test task 1')
        self.assertContains(response, 'Test task 2')
        self.assertNotContains(response, 'Test task 3')

        response = self.client.get(reverse('task_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Used label 1')
        self.assertContains(response, 'Status 1')
        self.assertContains(response, 'First Last')
        self.assertContains(response, 'Name Surname')
        self.assertNotContains(response, 'Used label 2')
        self.assertNotContains(response, 'Status 2')

        response = self.client.post(
            reverse('tasks_create'),
            data={
                'name': 'Test task 3',
                'description': 'Test some cases',
                'status': 1,
                'author': 2,
                'executor': 2,
                'labels': [1, 2]
            }
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('task_detail', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test task 3')
        self.assertContains(response, 'Test some cases')
        self.assertContains(response, 'Used label 1')
        self.assertContains(response, 'Used label 2')
        self.assertContains(response, 'Status 1')
        self.assertContains(response, 'First Last')
        self.assertContains(response, 'Name Surname')
        self.assertNotContains(response, 'Status 2')

        response = self.client.post(
            reverse('tasks_update', kwargs={'pk': 3}),
            data={
                'name': 'Test task 3',
                'description': 'Test new cases',
                'status': 1,
                'author': 2,
                'executor': 2,
                'labels': [1]
            }
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('task_detail', kwargs={'pk': 3}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test task 3')
        self.assertNotContains(response, 'Test some cases')
        self.assertContains(response, 'Test new cases')
        self.assertContains(response, 'Used label 1')
        self.assertNotContains(response, 'Used label 2')
        self.assertContains(response, 'Status 1')
        self.assertContains(response, 'First Last')
        self.assertContains(response, 'Name Surname')
        self.assertNotContains(response, 'Status 2')

        response = self.client.post(
            reverse('tasks_delete', kwargs={'pk': 2}),
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('tasks'))
        self.assertContains(response, 'Test task 1')
        self.assertContains(response, 'Test task 2')
        self.assertContains(response, 'Test task 3')
        self.assertContains(
            response,
            _('Задачу может удалить только ее автор')
        )

        response = self.client.post(
            reverse('tasks_delete', kwargs={'pk': 3}),
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('tasks'))
        self.assertContains(response, 'Test task 1')
        self.assertContains(response, 'Test task 2')
        self.assertNotContains(response, 'Test task 3')
