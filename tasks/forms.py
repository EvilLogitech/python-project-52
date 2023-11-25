from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    model = Task
    fields = [
        'name',
        'description',
        'executor',
        'status'
    ]
