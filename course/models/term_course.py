from django.db import models
from django_jalali.db import models as jmodels


class TermCourse(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name='term_course_course')
    term = models.ForeignKey(to='college.Term', on_delete=models.CASCADE, related_name='term_course_term')
    exam_date_time = jmodels.jDateTimeField()
    exam_venue = models.CharField(max_length=50)
    professor = models.ForeignKey(to='accounts.Professor', on_delete=models.CASCADE,
                                  related_name='term_course_professor')
    capacity = models.IntegerField()
    time = models.TimeField()
    day = models.IntegerField(
        choices=[(1, 'شنبه'), (2, 'یکشنبه'), (3, 'دوشنبه'), (4, 'سه شنبه'), (5, 'چهارشنبه'), (6, 'پنجشنبه'),
                 (7, 'جمعه')])

    def __str__(self):
        return self.course.name + ' - ' + self.term.name
