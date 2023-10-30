from django.contrib import admin
from .models import *
from shared.admin import *


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
