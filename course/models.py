from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Course(models.Model):
     name = models.CharField(max_length=50)
     faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE , related_name='faculty_course')
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
    term = models.ForeignKey(to='college.Term', on_delete=models.CASCADE , related_name='term_course')
    exam_date_time = jmodels.jDateTimeField()
    exam_venue = models.CharField(max_length=50)
    profossor = models.ForeignKey(to='accounts.Professor', on_delete=models.CASCADE , related_name='term_course')
    capacity = models.IntegerField()
    time = models.TimeField()
    day = models.IntegerField(choices=[(1, 'شنبه'), (2, 'یکشنبه'), (3, 'دوشنبه'), (4, 'سه شنبه'), (5, 'چهارشنبه'), (6, 'پنجشنبه'), (7, 'جمعه')])

    def __str__(self):
        return self.course.name + ' - ' + self.term.name


class StrudentCourse(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE , related_name='student_course')
    course_state = models.CharField(max_length=50 , choices=[ ('passed', 'قبول'), ('failed', 'مردود')])
    grade = models.IntegerField()
    term = models.ForeignKey(to='college.Term', on_delete=models.CASCADE , related_name='student_course')

    def __str__(self):
        return self.course.name + ' - ' + self.term.name