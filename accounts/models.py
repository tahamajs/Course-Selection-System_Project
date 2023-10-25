from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels


class General(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(General):
    user_no = models.IntegerField()
    avatar = models.ImageField(upload_to=lambda instance, filename: f'user_{instance.user.id}/{filename}')
    phone_number = models.CharField()
    national_code = models.CharField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birth_date = jmodels.jDateField()
