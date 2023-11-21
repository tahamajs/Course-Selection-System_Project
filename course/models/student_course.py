from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class StudentCourse(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='student_course_course',
                               verbose_name=_('نام درس'))
    course_state = models.CharField(max_length=50, choices=[('passed', 'قبول'), ('failed', 'مردود')],
                                    verbose_name=_('وضعیت درس'))
    grade = models.IntegerField(verbose_name=_('نمره دانشجو'))
    term = models.ForeignKey(to='college.Term', on_delete=models.CASCADE, related_name='student_course_term',
                             verbose_name=_('ترم اخذ شده'))

    def __str__(self):
        return self.course.name + ' - ' + self.term.name
