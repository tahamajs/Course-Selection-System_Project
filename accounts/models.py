from django.contrib.auth.models import AbstractUser
from django.db import models


class General(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(General):
    user_no = models.IntegerField()
    avatar = models.ImageField(upload_to=lambda instance, filename: f'user_{instance.user.id}/{filename}')
