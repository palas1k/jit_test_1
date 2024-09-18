from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskAPITestCase(APITestCase):
    def test_get_tasks(self):
        task1 = Task.objects.create(title='Task 1')
        task2 = Task.objects.create(title='Task 2')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        data = {'title': 'New Task'}
        response = self.client.post(reverse('tasks'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_get_task(self):
        task = Task.objects.create(title='Task 1')
        response = self.client.get(reverse('task-detail', args=[task.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task.title)

    def test_update_task(self):
        task = Task.objects.create(title='Task 1')
        data = {'title': 'Updated Task'}
        response = self.client.put(reverse('task-detail', args=[task.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=task.id).title, 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(title='Task 1')
        response = self.client.delete(reverse('task-detail', args=[task.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
