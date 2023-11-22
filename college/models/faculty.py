from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Faculty(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_('نام دانشکده'))

    def __str__(self):
        return self.name
