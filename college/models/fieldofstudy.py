from django.db import models
from .faculty import Faculty
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class FieldOfStudy(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_('نام رشته'))
    group = models.CharField(max_length=256, verbose_name=_('گروه آموزشی'))
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, related_name='field_of_study_faculty',
                                verbose_name=_('دانشکده'))
    units = models.IntegerField(verbose_name=_('تعداد واحد'))
    degree = models.CharField(max_length=256, verbose_name=_('مقطع'))

    def __str__(self):
        return self.name
