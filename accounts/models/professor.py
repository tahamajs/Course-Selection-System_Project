from django.db import models
from .user import User
from accounts.models.helper import Expertise
from accounts.models.helper import Degree


class Professor(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='professor_user')
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE, related_name='professor_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='professor_field_of_study')
    expertise = models.OneToOneField(to=Expertise, on_delete=models.CASCADE, related_name='professor_expertise')
    degree = models.OneToOneField(to=Degree, on_delete=models.CASCADE, related_name='professor_degree')
    past_teaching_courses = models.ManyToManyField(to='course.Course',
                                                   related_name='professor_past_courses', blank=True)

    def __str__(self):
        return self.user.username
