from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import UserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(username=form_data['username'], password=form_data['password'])
            if user:
                login(request, user)
                return redirect(reverse('index'))
        else:
            form = LoginUserForm()
        return render(request, 'users/login.html', {'form': form})


class LogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('index'))


# Create your views here.
class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/users.html', {'users': users})


class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/user_create_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect(reverse('login'))
        return render(request, 'users/user_create_form.html', {'form': form})


class UsersUpdateView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        if request.user.id != id:
            messages.error(request, _('У вас нет прав для изменения другого пользователя.'))
            return redirect(reverse('users'), request)
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
        return render(request, 'users/user_update_form.html', {'form': form, 'user': user})

    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        if request.user.id != id:
            return redirect(reverse('users'))
        user = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form_data = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(form_data['password1'])
            user.save()
            user = authenticate(username=form_data['username'], password=form_data['password1'])
            login(request, user)
            return redirect(reverse('users'))
        return render(request, 'users/user_update_form.html', {'form': form, 'user': user})


class UsersDeleteView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        if request.user.id != id:
            messages.info(request, _('Нельзя удалять не своего пользователя.'))
            return redirect(reverse('users'))
        user = User.objects.get(pk=id)
        return render(request, 'users/user_delete_form.html', {'user': user})

    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        if request.user.id != id:
            return redirect(reverse('users'))
        user = User.objects.get(pk=id)
        user.delete()
        return redirect(reverse('users'))
