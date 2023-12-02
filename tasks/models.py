from django.db import models
from statuses.models import Status
from labels.models import Label
from users.models import TaskManagerUser
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        verbose_name=_('Имя')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Описание')
    )
    author = models.ForeignKey(
        TaskManagerUser,
        on_delete=models.PROTECT,
        verbose_name=_('Автор'),
        related_name=_('Автор')
    )
    executor = models.ForeignKey(
        TaskManagerUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Исполнитель'),
        related_name=_('Исполнитель')
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name=_('Статус')
    )
    labels = models.ManyToManyField(
        Label,
        through='LabelsRelations',
        blank=True,
        verbose_name=_('Метка')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LabelsRelations(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    lables = models.ForeignKey(Label, on_delete=models.PROTECT)
