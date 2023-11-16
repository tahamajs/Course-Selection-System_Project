from django.db import models
from accounts.models import Student
from course.models.course import Course


class Registration(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='reg_student')
    courses = models.ManyToManyField(to=Course)
    approval_status = models.BooleanField(default=False)