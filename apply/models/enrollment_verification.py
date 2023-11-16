from django.db import models
from accounts.models import Student
from college.models import Term


class EnrollmentVerification(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='enrollment_verification_req_student')
    enrollment_verification_file = models.FileField()
    term = models.ForeignKey(to=Term, on_delete=models.CASCADE, related_name='enrollment_verification_req_term')
    issuance_certificate_place = models.CharField(max_length=200)
