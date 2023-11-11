from django.db import models
from accounts.models import Student
from college.models import Term


class TermDrop(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='term_drop_req_student')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_drop_req_term')
    student_descr = models.TextField(blank=True, null=True)
    educational_deputy_descr = models.TextField(blank=True, null=True)
