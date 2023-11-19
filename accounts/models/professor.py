from django.db import models
from .user import User
from .expertise import Expertise
from .degree import Degree
from shared.models import BaseModel


class Professor(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='professor_user')
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, related_name='professor_faculty')
    field_of_study = models.ForeignKey(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='professor_field_of_study')
    expertise = models.ForeignKey(to=Expertise, on_delete=models.CASCADE, related_name='professor_expertise')
    degree = models.ForeignKey(to=Degree, on_delete=models.CASCADE, related_name='professor_degree')
    past_teaching_courses = models.ManyToManyField(to='course.Course',
                                                   related_name='professor_past_courses', blank=True)

    def __str__(self):
        return self.user.username
