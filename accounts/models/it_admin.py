from django.db import models
from .faculty_user import FacultyUser


class ITAdmin(models.Model):
    user = models.OneToOneField(FacultyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.base_user.username
