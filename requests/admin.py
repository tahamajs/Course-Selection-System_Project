from django.contrib import admin
from .models import *
from shared.admin import *

admin.site.register(RegistrationReq, GeneralAdmin)
admin.site.register(UpdateTakenCourseReq, GeneralAdmin)
admin.site.register(CourseDropReq, GeneralAdmin)
admin.site.register(TermDropReq, GeneralAdmin)
admin.site.register(EnrollmentVerificationReq, GeneralAdmin)
admin.site.register(ReviewCourseReq, GeneralAdmin)
