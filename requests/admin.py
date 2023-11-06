from django.contrib import admin
from django.contrib.auth.models import Group
from requests.models import Registration, RegistrationUpdate, CourseDrop, TermDrop, ReviewGrade, \
    EnrollmentVerification


admin.site.register(Registration)
admin.site.register(RegistrationUpdate)
admin.site.register(CourseDrop)
admin.site.register(TermDrop)
admin.site.register(ReviewGrade)
admin.site.register(EnrollmentVerification)
