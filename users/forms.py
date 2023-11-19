from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-input'}))


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    password1 = forms.CharField(
        label='Пароль',
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя', 'required': 'true'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия', 'required': 'true'}),
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Введённые пароли не сопадают")
