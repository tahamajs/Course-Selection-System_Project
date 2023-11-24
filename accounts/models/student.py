from django.db import models
from django_jalali.db import models as jmodels
from .professor import Professor
from django.contrib.auth import get_user_model
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Student(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_('یوزر'))
    entry_year = jmodels.jDateField(verbose_name=_('سال ورودی'))
    entry_term = models.IntegerField(choices=((1, 'نیمه اول'), (2, 'نیمه دوم')), verbose_name=_('ترم ورودی'))
    gpa = models.DecimalField(max_digits=5, decimal_places=3, verbose_name=_('معدل'), null=True, blank=True)
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, related_name='student_faculty',
                                verbose_name=_('دانشکده'))
    field_of_study = models.ForeignKey(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                       related_name='student_field_of_study', verbose_name=_('رشته تحصیلی'))
    courses_passed = models.ManyToManyField(to='course.Course',
                                            related_name='student_courses_passed', blank=True,
                                            verbose_name=_('دروس گذرانده'))
    courses_taken = models.ManyToManyField(to='course.Course',
                                           related_name='student_courses_taken', verbose_name=_('دروس در حال گذراندن'))
    supervisor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name='student_supervisor',
                                   verbose_name=_('استاد راهنما'))
    military_service_status = models.CharField(max_length=3,
                                               choices=(
                                                   ('SBJ', 'مشمول'), ('MEE', 'معافیت تحصیلی'), ('MES', 'پایان خدمت')),
                                               verbose_name=_('وضعیت نظام وظیفه'))
    academic_years = models.IntegerField(verbose_name=_('سنوات'))

    def __str__(self):
        return self.user.username
