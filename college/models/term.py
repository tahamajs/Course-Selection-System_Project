from django.db import models
from django_jalali.db import models as jmodels
from shared.models import BaseModel


class Term(BaseModel):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField(to='accounts.Student', related_name='term_student', blank=True)
    professors = models.ManyToManyField(to='accounts.Professor', related_name='term_professor', blank=True)
    selection_start_time = jmodels.jDateTimeField()
    selection_end_time = jmodels.jDateTimeField()
    classes_start_time = jmodels.jDateTimeField()
    classes_end_time = jmodels.jDateTimeField()
    update_start_time = jmodels.jDateTimeField()
    update_end_time = jmodels.jDateTimeField()
    emergency_cancellation_end_time = jmodels.jDateTimeField()
    exams_start_time = jmodels.jDateField()
    term_end_time = jmodels.jDateField()

