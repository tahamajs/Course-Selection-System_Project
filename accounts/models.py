from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jalali.db import models as jmodels


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


class Professor(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='professor_user')
    college = models.OneToOneField(to='', on_delete=models.CASCADE, related_name='professor_college')
    field_of_study = models.ForeignKey(to='', on_delete=models.CASCADE, related_name='professor_field_of_study')
    expertise = models.ForeignKey(to='', on_delete=models.CASCADE, related_name='professor_expertise')
    degree = models.ForeignKey(to='', on_delete=models.CASCADE, related_name='professor_degree')


class ITAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models)


class EducationalDeputy(models.Model):
    user = models.OneToOneField(User, on_delete=models)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models)
    entry_year = jmodels.jDateField()
    entry_term = models.IntegerField(max_length=1, choices=((1, 'نیمه اول'), (2, 'نیمه دوم')))
    gpa = models.DecimalField(max_digits=5, decimal_places=3)  # معدل => grade point average
    college = models.ForeignKey(to='', on_delete=models.CASCADE, related_name='student_college')
    field_of_study = models.ForeignKey(to='', on_delete=models.CASCADE, related_name='student_field_of_study')
    courses_passed = models.ManyToManyField(to='', on_delete=models.CASCADE, related_name='student_courses_passed')
    courses_passing = models.ManyToManyField(to='', on_delete=models.CASCADE, related_name='student_courses_passing')
    supervisor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name='student_supervisor')
    military_service_status = models.CharField(
        choices=(('SBJ', 'مشمول'), ('MEE', 'معافیت تحصیلی'), ('MES', 'پایان خدمت')))
    years_of_education = models.IntegerField()
