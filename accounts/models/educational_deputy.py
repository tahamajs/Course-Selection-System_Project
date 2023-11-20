from django.db import models
from .user import User
from django.utils.translation import gettext_lazy as _


class EducationalDeputy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('یوزر'))
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE,
                                   related_name='educational_deputy_faculty', verbose_name=_('دانشکده'))
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='educational_deputy_field_of_study', verbose_name=_('رشته'))

    def __str__(self):
        return self.user.username
