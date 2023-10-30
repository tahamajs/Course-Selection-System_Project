from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels
from shared.models import *


class General(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(General):
    user_no = models.IntegerField()
    avatar = models.ImageField(upload_to=lambda instance, filename: f'user_{instance.user.id}/{filename}')
    phone_number = models.CharField()
    national_code = models.CharField()
    gender = models.CharField(max_length=1, choices=(('M', 'مرد'), ('F', 'زن')))
    birth_date = jmodels.jDateField()


class Expertise(models.Model):
    name = models.CharField(max_length=100)


class Degree(models.Model):
    name = models.CharField(max_length=100)


class Professor(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='professor_user')
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE, related_name='professor_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='professor_field_of_study')
    expertise = models.OneToOneField(to=Expertise, on_delete=models.CASCADE, related_name='professor_expertise')
    degree = models.OneToOneField(to=Degree, on_delete=models.CASCADE, related_name='professor_degree')
    past_teaching_courses = models.ManyToManyField(to='college.Course',
                                                   related_name='professor_courses')


class ITAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class EducationalDeputy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE,
                                   related_name='educational_deputy_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='educational_deputy_field_of_study')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entry_year = jmodels.jDateField()
    entry_term = models.IntegerField(max_length=1, choices=((1, 'نیمه اول'), (2, 'نیمه دوم')))
    gpa = models.DecimalField(max_digits=5, decimal_places=3)  # معدل => grade point average
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE, related_name='student_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='student_field_of_study')
    courses_passed = models.ManyToManyField(to='college.Course',
                                            related_name='student_courses_passed')
    courses_taken = models.ManyToManyField(to='college.Course',
                                           related_name='student_courses_passing')
    supervisor = models.OneToOneField(to=Professor, on_delete=models.CASCADE, related_name='student_supervisor')
    military_service_status = models.CharField(
        choices=(('SBJ', 'مشمول'), ('MEE', 'معافیت تحصیلی'), ('MES', 'پایان خدمت')))
    academic_years = models.IntegerField()
