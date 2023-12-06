from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import ContextMixin
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext as _
from .forms import UserForm
from .models import TaskManagerUser


class UserLoginView(LoginView):

    template_name = 'users/login.html'
    next_page = reverse_lazy('index')
    extra_context = {
        'title': _('Вход'),
        'button_value': _('Войти')
    }

    def form_valid(self, form):
        messages.success(self.request, _('Вы залогинены'))
        return super().form_valid(form)


class UserLogoutView(View):

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _('Вы разлогинены'))
        return redirect(reverse('index'))


class UsersListView(ListView, ContextMixin):
    model = TaskManagerUser
    template_name = 'users/users.html'
    extra_context = {'title': _('Пользователи')}


class UsersCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(
            request, 'users/user_create_form.html',
            {
                'form': form,
                'title': _('Регистрация'),
                'button_value': _('Зарегистрировать')
            }
        )

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.info(
                request,
                _('Пользователь успешно зарегистрирован')
            )
            return redirect(reverse('login'))
        return render(request, 'users/user_create_form.html', {'form': form})


class UsersUpdateView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        if not request.user.is_authenticated:
            messages.error(
                request, _('Вы не авторизованы! Пожалуйста, выполните вход.')
            )
            return redirect(reverse('login'), request)
        if request.user.id != id:
            messages.error(
                request,
                _('У вас нет прав для изменения другого пользователя.')
            )
            return redirect(reverse('login'), request)
        user = TaskManagerUser.objects.get(pk=id)
        form = UserForm(instance=user)
        return render(
            request,
            'users/user_update_form.html',
            {
                'form': form,
                'user': user,
                'title': _('Изменение пользователя'),
                'button_value': _('Изменить')
            }
        )

    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        if request.user.id != id:
            return redirect(reverse('users'))
        user = TaskManagerUser.objects.get(pk=id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form_data = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(form_data['password1'])
            user.save()
            user = authenticate(
                username=form_data['username'], password=form_data['password1']
            )
            login(request, user)
            messages.info(
                request,
                _('Пользователь успешно изменен')
            )
            return redirect(reverse('users'))
        return render(
            request,
            'users/user_update_form.html',
            {'form': form, 'user': user}
        )


class UsersDeleteView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        if not request.user.is_authenticated:
            messages.error(
                request, _('Вы не авторизованы! Пожалуйста, выполните вход.')
            )
            return redirect(reverse('login'), request)
        if request.user.id != id:
            messages.info(
                request, _('Нельзя удалять не своего пользователя.')
            )
            return redirect(reverse('login'), request)
        user = TaskManagerUser.objects.get(pk=id)
        return render(
            request,
            'users/user_delete_form.html',
            {
                'user': user,
                'title': _('Удаление пользователя'),
                'button_value': _('Да, удалить')
            }
        )

    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        if request.user.id != id:
            return redirect(reverse('users'))
        user = User.objects.get(pk=id)
        user.delete()
        messages.info(
            request,
            _('Пользователь успешно удален')
        )
        return redirect(reverse('users'))
