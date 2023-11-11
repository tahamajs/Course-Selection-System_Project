from django.db import models
from accounts.models import Student
from course.models.course import Course


class RegistrationUpdate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='update_taken_course_student')
    add_courses = models.ManyToManyField(Course, blank=True, related_name='update_taken_course_add')
    del_courses = models.ManyToManyField(Course, blank=True, related_name='update_taken_course_del')
    approval_status = models.BooleanField(default=False)
