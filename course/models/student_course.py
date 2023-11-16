from django.db import models
from shared.models import BaseModel
from .course import Course


class StudentCourse(BaseModel):
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='student_course_course')
    course_state = models.CharField(max_length=50, choices=[('passed', 'قبول'), ('failed', 'مردود')])
    grade = models.IntegerField()
    term = models.ForeignKey(to='college.Term', on_delete=models.CASCADE, related_name='student_course_term')

    def __str__(self):
        return self.course.name + ' - ' + self.term.name
