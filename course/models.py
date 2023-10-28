from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Course(models.Model):
     name = models.CharField(max_length=50)
     faculty = models.ForeignKey() # TODO: add faculty model
     prerequisite = models.ManyToManyField('self', blank=True)
     corequisite = models.ManyToManyField('self', blank=True)
     credits = models.IntegerField()
     course_type = models.CharField(max_length=50, choices=[
         ('core', 'عمومی'),
         ('specialized', 'تخصصی'),
         ('foundation', 'پایه'),
         ('elective', 'اختیاری'),
     ])
     def __str__(self):
         return self.name

class TermCourse(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE , related_name='term_course')
    term = models.ForeignKey() # TODO: add term model
    exam_date_time = jmodels.jDateTimeField()
    exam_venue = models.CharField(max_length=50)
    profossor = models.ForeignKey() # TODO: add Profossor model
    capacity = models.IntegerField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.course.name + ' - ' + self.term.name


class StrudentCourse(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE , related_name='student_course')
    course_state = models.CharField(max_length=50 , choices=[ ('passed', 'قبول'), ('failed', 'مردود')])
    grade = models.IntegerField()
    term = models.ForeignKey() # TODO: add term model

    def __str__(self):
        return self.course.name + ' - ' + self.term.name