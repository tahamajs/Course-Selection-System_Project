from django.db import models
from .user import User
from shared.models import BaseModel


class ITAdmin(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
