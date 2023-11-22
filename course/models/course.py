from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from shared.models import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('نام درس'))
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, related_name='course_faculty',
                                verbose_name=_('دانشکده ارایه دهنده'))
    pre_requisite = models.ManyToManyField('self', blank=True, verbose_name=_('پیش نیازها'))
    co_requisite = models.ManyToManyField('self', blank=True, verbose_name=_('هم نیازها'))
    credits = models.IntegerField(verbose_name=_('تعداد واحد درس'))
    course_type = models.CharField(max_length=50, choices=[
        ('core', 'عمومی'),
        ('specialized', 'تخصصی'),
        ('foundation', 'پایه'),
        ('elective', 'اختیاری'),
    ], verbose_name=_('نوع درس'))

    def __str__(self):
        return self.name
