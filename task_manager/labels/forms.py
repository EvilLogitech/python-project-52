from django import forms
from .models import Label


class LabelForm(forms.ModelForm):
    model = Label
    fields = ['name']
