from django.db import models
from accounts.models import Student
from course.models.course import Course


class ReviewGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='review_course_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review_course_course')
    review_text = models.TextField()
    result_text = models.TextField()