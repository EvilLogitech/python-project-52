from django.db.models import ProtectedError, RestrictedError
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _
from .models import Label


class LabelsListView(LoginRequiredMixin, ListView, ContextMixin):
    model = Label
    template_name = 'labels/labels.html'
    extra_context = {'title': _('Метки'), 'button_value': _('Создать метку')}


class LabelsCreateView(LoginRequiredMixin, SuccessMessageMixin,
                       CreateView, ContextMixin):
    model = Label
    fields = ['name']
    template_name = 'labels/label_create_form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно создана')
    extra_context = {
        'title':
        _('Создание метки'),
        'button_value': _('Создать')
    }


class LabelsUpdateView(LoginRequiredMixin, SuccessMessageMixin,
                       UpdateView, ContextMixin):
    model = Label
    fields = ['name']
    template_name = 'labels/label_update_form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно изменена')
    extra_context = {
        'title': _('Изменение метки'),
        'button_value': _('Изменить')
    }


class LabelsDeleteView(LoginRequiredMixin, SuccessMessageMixin,
                       DeleteView, ContextMixin):
    model = Label
    template_name = 'labels/label_delete_form.html'
    success_url = reverse_lazy('labels')
    success_message = _('Метка успешно удалена')
    extra_context = {
        'title': _('Удаление метки'),
        'button_value': _('Да, удалить')
    }

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except (ProtectedError, RestrictedError):
            messages.error(
                request,
                _('Невозможно удалить метку, потому что она используется')
            )
            return redirect(reverse('labels'))
