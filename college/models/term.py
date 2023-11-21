from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


class Term(models.Model):
    name = models.CharField(max_length=256, verbose_name=_('نام ترم'))
    students = models.ManyToManyField(to='accounts.Student', related_name='term_student', blank=True,
                                      verbose_name=_('دانشجو ها'))
    professors = models.ManyToManyField(to='accounts.Professor', related_name='term_professor', blank=True,
                                        verbose_name=_('اساتید'))
    selection_start_time = jmodels.jDateTimeField(verbose_name=_('زمان شروع انتخاب واحد'))
    selection_end_time = jmodels.jDateTimeField(verbose_name=_('زمان پایان انتخاب واحد'))
    classes_start_time = jmodels.jDateTimeField(verbose_name=_('زمان شروع کلاس ها'))
    classes_end_time = jmodels.jDateTimeField(verbose_name=_('زمان پایان کلاس ها'))
    update_start_time = jmodels.jDateTimeField(verbose_name=_('زمان شروع ترمیم'))
    update_end_time = jmodels.jDateTimeField(verbose_name=_('زمان پایان ترمیم'))
    emergency_cancellation_end_time = jmodels.jDateTimeField(verbose_name=_('زمان پایان حذف اضطراری'))
    exams_start_time = jmodels.jDateField(verbose_name=_('زمان شروع امتحانات'))
    term_end_time = jmodels.jDateField(verbose_name=_('زمان پایان ترم'))

    def __str__(self):
        return self.name
