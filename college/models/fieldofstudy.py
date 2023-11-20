from django.db import models
from .faculty import Faculty


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=256)
    group = models.CharField(max_length=256)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, related_name='field_of_study_faculty')
    units = models.IntegerField()
    degree = models.CharField(max_length=256)

    def __str__(self):
        return self.name

