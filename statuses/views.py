from django.db.models import ProtectedError, RestrictedError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _
from .models import Status


# # Create your views here.
class StatusesListView(LoginRequiredMixin, ListView, ContextMixin):
    model = Status
    template_name = 'statuses/statuses.html'
    extra_context = {'title': _('Статусы'), 'button_value': ('Создать статус')}


class StatusesCreateView(LoginRequiredMixin, CreateView, ContextMixin):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_create_form.html'
    success_url = reverse_lazy('statuses')
    extra_context = {'title': _('Статусы'), 'button_value': _('Создать')}


class StatusesUpdateView(LoginRequiredMixin, UpdateView, ContextMixin):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_update_form.html'
    success_url = reverse_lazy('statuses')
    extra_context = {'title': _('Статусы'), 'button_value': _('Изменить')}


class StatusesDeleteView(LoginRequiredMixin, DeleteView, ContextMixin):
    model = Status
    template_name = 'statuses/status_delete_form.html'
    success_url = reverse_lazy('statuses')
    extra_context = {'title': _('Статусы'), 'button_value': _('Удалить')}

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except (ProtectedError, RestrictedError):
            messages.error(request, _('Невозможно удалить статус, потому что он используется'))
            return redirect(reverse('statuses'))
