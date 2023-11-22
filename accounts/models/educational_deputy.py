from django.db import models
from django.contrib.auth import get_user_model
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class EducationalDeputy(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_('یوزر'))
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE,
                                   related_name='educational_deputy_faculty', verbose_name=_('دانشکده'))
    field_of_study = models.ForeignKey(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='educational_deputy_field_of_study', verbose_name=_('رشته'))

    def __str__(self):
        return self.user.username
