from django.db import models
from .user import User
from accounts.models.helper import Expertise
from accounts.models.helper import Degree
from django.utils.translation import gettext_lazy as _


class Professor(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='professor_user',
                                verbose_name=_('یوزر'))
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE, related_name='professor_faculty',
                                   verbose_name=_('دانشکده'))
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='professor_field_of_study', verbose_name=_('رشته'))
    expertise = models.OneToOneField(to=Expertise, on_delete=models.CASCADE, related_name='professor_expertise',
                                     verbose_name=_('تخصص'))
    degree = models.OneToOneField(to=Degree, on_delete=models.CASCADE, related_name='professor_degree',
                                  verbose_name=_('مرتبه'))
    past_teaching_courses = models.ManyToManyField(to='course.Course',
                                                   related_name='professor_past_courses', blank=True,
                                                   verbose_name=_('دروس تدریسی گذشته'))

    def __str__(self):
        return self.user.username
