from django.db import models
from shared.models import BaseModel


class Faculty(BaseModel):
    name = models.CharField(max_length=256)
