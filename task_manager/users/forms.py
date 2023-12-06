from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class LoginUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    username = forms.CharField(
        label=_('Имя пользователя'),
        widget=forms.TextInput(
            attrs={'placeholder': _('Имя пользователя'), 'class': 'form-input'}
        )
    )
    password = forms.CharField(
        label=_('Пароль'),
        widget=forms.PasswordInput(
            attrs={'placeholder': _('Пароль'), 'class': 'form-input'}
        )
    )


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    password1 = forms.CharField(
        label=_('Пароль'),
        help_text=_('Ваш пароль должен содержать как минимум 3 символа.'),
        widget=forms.PasswordInput(attrs={'placeholder': _('Пароль')})
    )
    password2 = forms.CharField(
        label=_('Подтверждение пароля'),
        help_text=_('Для подтверждения введите, пожалуйста, пароль ещё раз.'),
        widget=forms.PasswordInput(
            attrs={'placeholder': _('Подтверждение пароля')}
        )
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': _('Имя'), 'required': 'true'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': _('Фамилия'), 'required': 'true'}
            ),
            'username': forms.TextInput(
                attrs={'placeholder': _('Имя пользователя')}
            ),
        }

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError(_('Введённые пароли не сопадают'))
