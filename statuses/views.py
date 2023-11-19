from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Status


# # Create your views here.
class StatusesListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/statuses.html', {'statuses': statuses})


class StatusesCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_create_form.html'
    success_url = reverse_lazy('statuses')


class StatusesUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/status_update_form.html'
    success_url = reverse_lazy('statuses')


class StatusesDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/status_delete_form.html'
    success_url = reverse_lazy('statuses')


def index(request):
    return HttpResponse('YOLO')
