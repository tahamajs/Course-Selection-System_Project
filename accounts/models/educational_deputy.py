from django.db import models
from django.contrib.auth import get_user_model
from .user import User
from shared.models import BaseModel

User = get_user_model()


class EducationalDeputy(BaseModel):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE,
                                   related_name='educational_deputy_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='educational_deputy_field_of_study')

    def __str__(self):
        return self.user.username
