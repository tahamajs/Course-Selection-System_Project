from django.db import models
from django_jalali.db import models as jmodels
from .professor import Professor
from .user import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entry_year = jmodels.jDateField()
    entry_term = models.IntegerField(choices=((1, 'نیمه اول'), (2, 'نیمه دوم')))
    gpa = models.DecimalField(max_digits=5, decimal_places=3)  # معدل => grade point average
    faculty = models.OneToOneField(to='college.Faculty', on_delete=models.CASCADE, related_name='student_faculty')
    field_of_study = models.OneToOneField(to='college.FieldOfStudy', on_delete=models.CASCADE,
                                          related_name='student_field_of_study')
    courses_passed = models.ManyToManyField(to='course.Course',
                                            related_name='student_courses_passed', blank=True)
    courses_taken = models.ManyToManyField(to='course.Course',
                                           related_name='student_courses_taken')
    supervisor = models.ForeignKey(to=Professor, on_delete=models.CASCADE, related_name='student_supervisor')
    military_service_status = models.CharField(max_length=3,
                                               choices=(
                                                   ('SBJ', 'مشمول'), ('MEE', 'معافیت تحصیلی'), ('MES', 'پایان خدمت')))
    academic_years = models.IntegerField()

    def __str__(self):
        return self.user.username
