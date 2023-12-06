from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Label(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        verbose_name=_('Имя')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Метка')
        verbose_name_plural = _('Метки')
