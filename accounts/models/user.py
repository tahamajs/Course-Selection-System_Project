from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels


def upload_dir(instance, filename):
    return f'uploads/user_{instance.base_user.username}_{instance.base_user.id}/{filename}'


class User(AbstractUser):
    user_no = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_dir, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    national_code = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'مرد'), ('F', 'زن')), null=True, blank=True)
    birth_date = jmodels.jDateField(null=True, blank=True)


    def __str__(self):
        return self.username
