from django.db import models
from statuses.models import Status
from labels.models import Label
from users.models import TaskManagerUser


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(TaskManagerUser, on_delete=models.PROTECT, related_name="author")
    executor = models.ForeignKey(TaskManagerUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="executor")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, blank=False)
    labels = models.ManyToManyField(Label, through='LabelsRelations', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LabelsRelations(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    lables = models.ForeignKey(Label, on_delete=models.PROTECT)
