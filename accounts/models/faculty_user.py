from django.db import models
from django_jalali.db import models as jmodels
from .user import User


def upload_dir(instance, filename):
    return f'uploads/user_{instance.base_user.username}_{instance.base_user.id}/{filename}'


class FacultyUser(models.Model):
    base_user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user_base_user')
    user_no = models.IntegerField()
    avatar = models.ImageField(upload_to=upload_dir)
    phone_number = models.CharField(max_length=12)
    national_code = models.CharField(max_length=12)
    gender = models.CharField(max_length=1, choices=(('M', 'مرد'), ('F', 'زن')))
    birth_date = jmodels.jDateField()

    def __str__(self):
        return self.base_user.username
