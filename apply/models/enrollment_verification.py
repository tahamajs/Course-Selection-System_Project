from django.db import models
from accounts.models import Student
from college.models import Term
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel


class EnrollmentVerification(BaseModel):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='enrollment_verification_req_student',
                                verbose_name=_('دانشجو'))
    enrollment_verification_file = models.FileField(verbose_name=_('فایل اشتغال به تحصیل'))
    term = models.ForeignKey(to=Term, on_delete=models.CASCADE, related_name='enrollment_verification_req_term',
                             verbose_name=_('ترم'))
    issuance_certificate_place = models.CharField(max_length=200, verbose_name=_('محل صدور گواهی'))
