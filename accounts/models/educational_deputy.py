from django.db import models
from django.contrib.auth import get_user_model
from shared.models import BaseModel

User = get_user_model()


class EducationalDeputy(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE,
                                   related_name='educational_deputy_faculty')
    field_of_study = models.ForeignKey(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='educational_deputy_field_of_study')

    def __str__(self):
        return self.user.username
