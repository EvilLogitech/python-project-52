from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UsersCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
    
    first_name = forms.CharField(label='Имя', max_length=100, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_password(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Passowrds are not same")
        return data['password1']


class UsersUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
    
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_password(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Passowrds are not same")
        return data['password1']
