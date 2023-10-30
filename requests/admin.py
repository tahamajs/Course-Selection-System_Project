from django.contrib import admin
from .models import *
from shared.admin import *

admin.site.register(RegistrationReq, admin.ModelAdmin)
admin.site.register(UpdateTakenCourseReq, admin.ModelAdmin)
admin.site.register(CourseDropReq, admin.ModelAdmin)
admin.site.register(TermDropReq, admin.ModelAdmin)
admin.site.register(EnrollmentVerificationReq, admin.ModelAdmin)
admin.site.register(ReviewCourseReq, admin.ModelAdmin)
