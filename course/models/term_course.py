from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class TermCourse(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='term_course_course',
                               verbose_name=_('نام درس'))
    term = models.ForeignKey(to='college.Term', on_delete=models.CASCADE, related_name='term_course_term',
                             verbose_name=_('ترم تحصیلی'))
    exam_date_time = jmodels.jDateTimeField(verbose_name=_('زمان امتحان'))
    exam_venue = models.CharField(max_length=50, verbose_name=_('مکان امتحان'))
    professor = models.ForeignKey(to='accounts.Professor', on_delete=models.CASCADE,
                                  related_name='term_course_professor', verbose_name=_('استاد درس'))
    capacity = models.IntegerField(verbose_name=_('ظرفیت درس'))
    time = models.TimeField(verbose_name=_('زمان'))
    day = models.IntegerField(
        choices=[(1, 'شنبه'), (2, 'یکشنبه'), (3, 'دوشنبه'), (4, 'سه شنبه'), (5, 'چهارشنبه'), (6, 'پنجشنبه'),
                 (7, 'جمعه')], verbose_name=_('روز'))

    def __str__(self):
        return self.course.name + ' - ' + self.term.name
