from django_filters.views import FilterView
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from task_manager.users.models import TaskManagerUser
from .models import Task
from .filters import TaskFilter
from .forms import TaskForm


class TasksListView(LoginRequiredMixin, FilterView, ContextMixin):
    model = Task
    filterset_class = TaskFilter
    form_class = TaskForm
    template_name = 'tasks/tasks.html'
    extra_context = {
        'title': _('Задачи'),
        'button_value': ('Создать задачу'),
        'button_filter_value': _('Показать')
    }


class TasksCreateView(LoginRequiredMixin, SuccessMessageMixin,
                      CreateView, ContextMixin):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Задача успешно создана')
    extra_context = {
        'title': _('Создать задачу'),
        'button_value': _('Создать')
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = TaskManagerUser.objects.get(pk=user.id)
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, SuccessMessageMixin,
                      UpdateView, ContextMixin):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Задача успешно изменена')
    extra_context = {
        'title': _('Изменение задачи'),
        'button_value': _('Изменить')
    }


class TasksDeleteView(LoginRequiredMixin, SuccessMessageMixin,
                      DeleteView, ContextMixin):
    model = Task
    template_name = 'tasks/task_delete_form.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Задача успешно удалена')
    extra_context = {
        'title': _('Удаление задачи'),
        'button_value': _('Да, удалить')
    }

    def dispatch(self, request, *args, **kwargs):
        current_user = self.request.user
        print(request.POST)
        task = Task.objects.get(pk=kwargs.get('pk'))
        if current_user.pk == task.author.pk:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, _('Задачу может удалить только ее автор'))
            return redirect(reverse('tasks'))


class TaskDetailedView(DetailView, ContextMixin):
    model = Task
    template_name = 'tasks/task.html'
    extra_context = {'title': _('Просмотр задачи')}
