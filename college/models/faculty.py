from django.db import models
from django.utils.translation import gettext_lazy as _


class Faculty(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('نام دانشکده'))

    def __str__(self):
        return self.name
