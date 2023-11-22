from django.db import models
from accounts.models import Student
from course.models.course import Course
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel


class RegistrationUpdate(BaseModel):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='update_taken_course_student',
                                verbose_name=_('دانشجو'))
    add_courses = models.ManyToManyField(to=Course, blank=True, related_name='update_taken_course_add',
                                         verbose_name=_('دروس اضافه'))
    del_courses = models.ManyToManyField(to=Course, blank=True, related_name='update_taken_course_del',
                                         verbose_name=_('دروس حذف'))
    approval_status = models.CharField(max_length=1,
                                       choices=[['E', 'درحال انجام توسط دانشجو'], ['P', 'منتظر نظر استاد'],
                                                ['A', 'تایید شده'], ['D', 'رد شده']], default='E',
                                       verbose_name=_('وضعیت تایید'))

    def __str__(self):
        return f'{self.student}-{self.id}'
