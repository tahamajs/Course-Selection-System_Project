from django.db import models
from .user import User
from django.utils.translation import gettext_lazy as _


class ITAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('یوزر'))

    def __str__(self):
        return self.user.username
