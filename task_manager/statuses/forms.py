from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    model = Status
    fields = ['name']
