from django.db import models
from accounts.models import Student
from course.models.course import Course
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel



class CourseDrop(BaseModel):
    choice = (
        ('1', 'تایید'),
        ('2', 'رد درخواست'),
        ('3', 'در حال بررسی')
    )
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='course_drop_req_student',
                                verbose_name=_('دانشجو'))
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, related_name='course_drop_req_course',
                               verbose_name=_('درس'))
    course_drop_status = models.IntegerField(choices=choice, default=3, verbose_name=_('نتیجه ی درخواست'))
    student_description = models.TextField(null=True, blank=True, verbose_name=_('توضیحات دانشجو'))
    educational_deputy_description = models.TextField(null=True, blank=True, verbose_name=_('توضیحات معاون آموزشی'))
