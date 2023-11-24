from shared.admin import *
from .models import *
from course.models import TermCourse
from accounts.models import Student, Professor
from django_jalali import admin as jadmin



class TermInline(admin.TabularInline):
    model = TermCourse



class TermAdmin(admin.ModelAdmin):
    model = Term
    inlines = [TermInline, ]


admin.site.register(Faculty, admin.ModelAdmin)
admin.site.register(FieldOfStudy, admin.ModelAdmin)
admin.site.register(Term, TermAdmin)
