from django.db import models
from accounts.models import Student
from course.models import Course
from college.models import Term


class RegistrationReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reg_student')
    courses = models.ManyToManyField(Course)
    approval_status = models.BooleanField(default=False)


class UpdateTakenCourseReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='update_taken_course_student')
    add_courses = models.ManyToManyField(Course, null=True, blank=True)
    del_courses = models.ManyToManyField(Course, null=True, blank=True)
    approval_status = models.BooleanField(default=False)


class CourseDropReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_drop_req_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_drop_req_course')
    student_descr = models.TextField(null=True, blank=True)
    educational_deputy_descr = models.TextField(null=True, blank=True)


class TermDropReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='term_drop_req_student')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_drop_req_term')
    student_descr = models.TextField(blank=True, null=True)
    educational_deputy_descr = models.TextField(blank=True, null=True)


class ReviewCourseReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='review_course_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review_course_course')
    req_text = models.TextField()
    result_text = models.TextField()


class EnrollmentVerificationReq(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment_verification_req_student')
    enrollment_verification_file = models.FileField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='enrollment_verification_req_term')
    issuance_certificate_place = models.CharField()
