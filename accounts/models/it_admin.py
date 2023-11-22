from django.db import models
from django.contrib.auth import get_user_model
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ITAdmin(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
