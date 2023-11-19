from django import forms
from statuses.models import Status


class StatusForm(forms.ModelForm):
    model = Status
    fields = ['name']
