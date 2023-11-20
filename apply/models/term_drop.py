from django.db import models
from accounts.models import Student
from college.models import Term
from django.utils.translation import gettext_lazy as _


class TermDrop(models.Model):
    choice = (
        ('1', 'تایید'),
        ('2', 'رد درخواست'),
        ('3', 'در حال بررسی')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='term_drop_req_student',
                                verbose_name=_('دانشجو'))
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_drop_req_term', verbose_name=_('ترم'))
    term_drop_status = models.IntegerField(choices=choice, verbose_name=_('نتیجه درخواست'), default=3)
    student_descr = models.TextField(blank=True, null=True, verbose_name=_('توضیحات دانشجو'))
    educational_deputy_descr = models.TextField(blank=True, null=True, verbose_name=_('توضیحات معاون آموزشی'))
