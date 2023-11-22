from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    user_no = models.IntegerField(null=True, blank=True, verbose_name=_('شماره کاربری'))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_('عکس پروفایل'))
    phone_number = models.CharField(max_length=12, null=True, blank=True, verbose_name=_('شماره تلفن'))
    national_code = models.CharField(max_length=12, null=True, blank=True, verbose_name=_('کد ملی'))
    gender = models.CharField(max_length=1, choices=(('M', 'مرد'), ('F', 'زن')), null=True, blank=True,
                              verbose_name=_('جنسیت'))
    birth_date = jmodels.jDateField(null=True, blank=True, verbose_name=_('تاریخ تولد'))

    def __str__(self):
        return self.username
