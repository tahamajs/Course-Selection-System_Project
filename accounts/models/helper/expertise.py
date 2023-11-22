from django.db import models
from shared.models import BaseModel


class Expertise(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
