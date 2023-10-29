from django.db import models
from accounts.models import Student
from courses.models import Course
from faculties.models import Term


class RegistrationReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    approval_status = models.BooleanField(default=False)


class UpdateTakenCourseReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    add_courses = models.ManyToManyField(Course, null=True, blank=True)
    del_courses = models.ManyToManyField(Course, null=True, blank=True)
    approval_status = models.BooleanField(default=False)


class CourseDropReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_descr = models.TextField(null=True, blank=True)
    educational_deputy_descr = models.TextField(null=True, blank=True)


class TermDropReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    student_descr = models.TextField(blank=True, null=True)
    educational_deputy_descr = models.TextField(blank=True, null=True)


class ReviewCourseReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    req_text = models.TextField()
    result_text = models.TextField()


class EnrollmentVerificationReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_verification_file = models.FileField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    issuance_certificate_place = models.CharField()


