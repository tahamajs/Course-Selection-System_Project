from django.db import models


class Term(models.Model):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField(to='accounts.Student', related_name='term_student', null=True, blank=True)
    professors = models.ManyToManyField(to='accounts.Professor', related_name='term_professor', null=True, blank=True)
    selection_start_time = models.DateTimeField()
    selection_end_time = models.DateTimeField()
    classes_start_time = models.DateTimeField()
    classes_end_time = models.DateTimeField()
    update_start_time = models.DateTimeField()
    update_end_time = models.DateTimeField()
    emergency_cancellation_end_time = models.DateTimeField()
    exams_start_time = models.DateField()
    term_end_time = models.DateField()
