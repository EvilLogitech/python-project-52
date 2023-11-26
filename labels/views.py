from django.db.models import ProtectedError, RestrictedError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _
from .models import Label


# # Create your views here.
class LabelsListView(LoginRequiredMixin, ListView, ContextMixin):
    model = Label
    template_name = 'labels/labels.html'
    extra_context = {'title': _('Метки'), 'button_value': _('Создать метку')}


class LabelsCreateView(LoginRequiredMixin, CreateView, ContextMixin):
    model = Label
    fields = ['name']
    template_name = 'labels/label_create_form.html'
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Создание метки'), 'button_value': _('Создать')}


class LabelsUpdateView(LoginRequiredMixin, UpdateView, ContextMixin):
    model = Label
    fields = ['name']
    template_name = 'labels/label_update_form.html'
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Изменение'), 'button_value': _('Изменить')}


class LabelsDeleteView(LoginRequiredMixin, DeleteView, ContextMixin):
    model = Label
    template_name = 'labels/label_delete_form.html'
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Удаление метки'), 'button_value': _('Удалить')}

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except (ProtectedError, RestrictedError):
            messages.error(request, _('Невозможно удалить метку, потому что она используется'))
            return redirect(reverse('labels'))
