from django.db import models
from statuses.models import Status
from users.models import TaskManagerUser


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(TaskManagerUser, on_delete=models.PROTECT, related_name="author")
    executor = models.ForeignKey(TaskManagerUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="executor")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, blank=False)
    # labels = models.ManyToManyField('Labels')
    created_at = models.DateTimeField(auto_now=True)
