from django.contrib import admin
from django.contrib.auth.models import Group
from requests.models import Registration, RegistrationUpdate, CourseDrop, TermDrop, ReviewGrade, \
    EnrollmentVerification

admin.register(Registration)
admin.register(RegistrationUpdate)
admin.register(CourseDrop)
admin.register(TermDrop)
admin.register(ReviewGrade)
admin.register(EnrollmentVerification)
