from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=256)


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=256)
    group = models.CharField(max_length=256)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, related_name='FOS')
    units = models.IntegerField()
    degree = models.CharField(max_length=256)


class Term(models.Model):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField(to='accounts.models.Student', related_name='terms')
    professors = models.ManyToManyField(to='accounts.models.Professor', related_name='terms')
    TermCourses = models.ManyToManyField(to='courses.models.TermCourse', related_name='terms')
    selection_start_time = models.DateTimeField()
    selection_end_time = models.DateTimeField()
    classes_start_time = models.DateTimeField()
    classes_end_time = models.DateTimeField()
    update_start_time = models.DateTimeField()
    update_end_time = models.DateTimeField()
    emergency_cancellation_end_time = models.DateTimeField()
    exams_start_time = models.DateField()
    term_end_time = models.DateField()
