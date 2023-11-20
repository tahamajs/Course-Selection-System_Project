from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, related_name='course_faculty')
    pre_requisite = models.ManyToManyField('self', blank=True)
    co_requisite = models.ManyToManyField('self', blank=True)
    credits = models.IntegerField()
    course_type = models.CharField(max_length=50, choices=[
        ('core', 'عمومی'),
        ('specialized', 'تخصصی'),
        ('foundation', 'پایه'),
        ('elective', 'اختیاری'),
    ])

    def __str__(self):
        return self.name
