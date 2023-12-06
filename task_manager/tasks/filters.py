import django_filters
from django.forms import CheckboxInput
from django.utils.translation import gettext as _
from task_manager.labels.models import Label
from .models import Task


class TaskFilter(django_filters.FilterSet):

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Метка")
    )
    own_tasks = django_filters.BooleanFilter(
        label=_('Только свои задачи'),
        method='get_authenticated_user_tasks', widget=CheckboxInput
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']

    def get_authenticated_user_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user)
