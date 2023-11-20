from django.db import models
from accounts.models import Student
from course.models.course import Course


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reg_student')
    courses = models.ManyToManyField(Course)
    approval_status = models.BooleanField(default=False)
