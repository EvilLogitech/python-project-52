from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponse
from .forms import UsersCreateForm, UsersUpdateForm
from django.contrib.auth.models import User


# Create your views here.
class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.exclude(pk=1)
        return render(request, 'users/users.html', {'users': users})


class UsersCreateView(CreateView):
    form_class = UsersCreateForm
    template_name = 'users/user_create_form.html'
    success_url = reverse_lazy('index')

    # def get(self, request, *args, **kwargs):
    #     form = UsersCreateForm()
    #     return render(request, 'users/user-add.html', {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = UsersCreateForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.set_password(form.cleaned_data['password1'])
    #         user.save()
    #         return redirect(reverse('index'))
    #     return render(request, 'users/user-add.html', {'form': form})


class UsersUpdateView(UpdateView):
    form_class = UsersUpdateForm
    model = User
    template_name = 'users/user_update_form.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        user = form.save()
        return render(request, 'users/user-edit.html', {'form': form, 'user': user})

    # fields = ['first_name', 'last_name', 'username', 'password', 'password2']

    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     user = User.objects.get(pk=id)
    #     form = UsersUpdateForm(instance=user)
    #     return render(request, 'users/user-edit.html', {'form': form, 'user': user})

    # def post(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     user = User.objects.get(pk=id)
    #     form = UsersCreateForm(request.POST, instance=user)
    #     return render(request, 'users/user-edit.html', {'form': form, 'user': user})


class UsersDeleteView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        return HttpResponse(f'/users/{id}/delete/ - GET')

    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        return HttpResponse(f'/users/{id}/delete/ - POST')
