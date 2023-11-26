from django import forms
from statuses.models import Label


class LabelForm(forms.ModelForm):
    model = Label
    fields = ['name']
