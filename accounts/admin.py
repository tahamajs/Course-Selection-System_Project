from .models import *
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(User, admin.ModelAdmin)

admin.site.register(Professor, admin.ModelAdmin)

admin.site.register(ITAdmin, admin.ModelAdmin)

admin.site.register(EducationalDeputy, admin.ModelAdmin)

admin.site.register(Student, admin.ModelAdmin)
