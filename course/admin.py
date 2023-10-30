from django.contrib import admin
from .models import Course, TermCourse, StudentCourse


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'credits', 'course_type')
    list_filter = ('faculty', 'course_type')
    search_fields = ('name',)


@admin.register(TermCourse)
class TermCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'term', 'exam_date_time', 'professor', 'capacity', 'time', 'day')
    list_filter = ('course', 'term', 'professor', 'day')
    search_fields = ('course__name', 'term__name', 'professor__user__username')


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'term', 'course_state', 'grade')
    list_filter = ('course', 'term', 'course_state')
    search_fields = ('course__name', 'term__name')


