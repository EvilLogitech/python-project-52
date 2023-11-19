from django.http import HttpResponse
from django.views import View


class TasksListView(View):
    def get(self):
        return HttpResponse('Yolo')


class TasksCreateView(View):
    def get(self):
        return HttpResponse('Yolo')


class TasksUpdateView(View):
    def get(self):
        return HttpResponse('Yolo')


class TasksDeleteView(View):
    def get(self):
        return HttpResponse('Yolo')
