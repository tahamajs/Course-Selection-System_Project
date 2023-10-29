from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import *


class GeneralAdmin(BaseUserAdmin):
    search_fields = list_display = ('__all__',)


class UserAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(User, UserAdmin)


class ExpertiseAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(Expertise, ExpertiseAdmin)


class DegreeAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(Degree, DegreeAdmin)


class ProfessorAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(Professor, ProfessorAdmin)


class ITAdminAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(ITAdmin, ITAdminAdmin)


class EducationalDeputyAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(EducationalDeputy, EducationalDeputyAdmin)


class StudentAdmin(GeneralAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(Student, StudentAdmin)
