from django.db import models
from .faculty_user import FacultyUser
from .expertise import Expertise
from .degree import Degree


class Professor(models.Model):
    user = models.OneToOneField(to=FacultyUser, on_delete=models.CASCADE, related_name='professor_user')
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE, related_name='professor_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='professor_field_of_study')
    expertise = models.OneToOneField(to=Expertise, on_delete=models.CASCADE, related_name='professor_expertise')
    degree = models.OneToOneField(to=Degree, on_delete=models.CASCADE, related_name='professor_degree')
    past_teaching_courses = models.ManyToManyField(to='course.Course',
                                                   related_name='professor_past_courses')

    def __str__(self):
        return self.user.base_user.username
