from django.contrib import admin
from .models import *
from shared.admin import *

admin.site.register(User, admin.ModelAdmin)

admin.site.register(Expertise, admin.ModelAdmin)

admin.site.register(Degree, admin.ModelAdmin)

admin.site.register(Professor, admin.ModelAdmin)

admin.site.register(ITAdmin, admin.ModelAdmin)

admin.site.register(EducationalDeputy, admin.ModelAdmin)

admin.site.register(Student, admin.ModelAdmin)
