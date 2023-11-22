from django.db import models
from accounts.models import Student
from course.models.course import Course
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel


class ReviewGrade(BaseModel):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='review_course_student',
                                verbose_name=_('دانشجو'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review_course_course',
                               verbose_name=_('درس'))
    review_text = models.TextField(null=True, blank=True, verbose_name=_('متن تجدیدنظر'))
    result_text = models.TextField(null=True, blank=True, verbose_name=_('پاسخ تجدیدنظر'))
