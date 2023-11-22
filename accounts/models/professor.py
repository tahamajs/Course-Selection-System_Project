from django.db import models
from django.contrib.auth import get_user_model
from shared.models import BaseModel
from accounts.models.helper.expertise import Expertise
from accounts.models.helper.degree import Degree
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Professor(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='professor_user',
                             verbose_name=_('یوزر'))
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, related_name='professor_faculty',
                                verbose_name=_('دانشکده'),null=True, blank=True)
    field_of_study = models.ForeignKey(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                       related_name='professor_field_of_study', verbose_name=_('رشته'))
    expertise = models.ForeignKey(to=Expertise, on_delete=models.CASCADE, related_name='professor_expertise',
                                  verbose_name=_('تخصص'))
    degree = models.ForeignKey(to=Degree, on_delete=models.CASCADE, related_name='professor_degree',
                               verbose_name=_('مرتبه'))
    past_teaching_courses = models.ManyToManyField(to='course.Course',
                                                   related_name='professor_past_courses', blank=True,
                                                   verbose_name=_('دروس تدریسی گذشته'))

    def __str__(self):
        return f'{self.user.name}'

    class Meta:
        ordering = ('pk',)
