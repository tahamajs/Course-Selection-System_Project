from django.db import models
from accounts.models import Student
from course.models.course import Course


class CourseDrop(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_drop_req_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_drop_req_course')
    student_description = models.TextField(null=True, blank=True)
    educational_deputy_description = models.TextField(null=True, blank=True)
