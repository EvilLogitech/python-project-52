from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from users.models import TaskManagerUser
from .models import Task
from .forms import TaskForm
from django.utils.translation import gettext as _


class TasksListView(LoginRequiredMixin, ListView, ContextMixin):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/tasks.html'
    extra_context = {'title': _('Задачи'), 'button_value': ('Создать задачу')}


class TasksCreateView(LoginRequiredMixin, CreateView, ContextMixin):
    model = Task
    form = TaskForm
    form_class = TaskForm
    template_name = 'tasks/task_create_form.html'
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Создать задачу'), 'button_value': _('Создать')}

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = TaskManagerUser.objects.get(pk=user.id)
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, UpdateView, ContextMixin):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update_form.html'
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Изменение задачи'), 'button_value': _('Изменить')}


class TasksDeleteView(LoginRequiredMixin, DeleteView, ContextMixin):
    model = Task
    template_name = 'tasks/task_delete_form.html'
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Удаление задачи'), 'button_value': _('Удалить')}

    def dispatch(self, request, *args, **kwargs):
        current_user = self.request.user
        print(request.POST)
        task = Task.objects.get(pk=kwargs.get('pk'))
        if current_user.pk == task.author.pk:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, _('Задачу может удалить только её автор'))
            return redirect(reverse('tasks'))


class TaskDetailedView(DetailView, ContextMixin):
    model = Task
    template_name = 'tasks/task.html'
    extra_context = {'title': _('Просмотр задачи')}
