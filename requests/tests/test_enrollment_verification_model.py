from django.test import TestCase
from accounts.models import Student, User, Professor, Expertise, Degree, FacultyUser
from college.models import FieldOfStudy, Faculty, Term
from requests.models.enrollment_verification import EnrollmentVerification
from course.models.course import Course
from django.core.files.uploadedfile import SimpleUploadedFile
from django_jalali import date


class EnrollmentVerificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                               degree='کارشناسی')
        self.passed_courses = [Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                     credits=3, course_type='core'), ]
        self.taken_courses = [Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                    credits=3, course_type='specialized'), ]

        avatar = SimpleUploadedFile(name='test_image.jpg',
                                    content=open(r"C:\Users\Asus\Pictures\Screenshots\Screenshot (163).png",
                                                 'rb').read(),
                                    content_type='image/jpeg')
        self.faculty_user = FacultyUser.objects.create(base_user=self.user, user_no=5214, avatar=avatar,
                                                       phone_number='+987654321', national_code='1547825478',
                                                       gender='M',
                                                       birth_date='1375-05-08')
        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.faculty_user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.faculty_user, entry_year='1375-10-10', entry_term=1, gpa=18.0,
                                              faculty=self.faculty, field_of_study=self.fos, supervisor=self.professor,
                                              military_service_status='SBJ',
                                              academic_years=2)
        self.student.courses_passed.add(*self.passed_courses)
        self.student.courses_taken.add(*self.taken_courses)
         
        # needs to be completed
        self.term = Term.objects.create(
            name="Spring Term",
            selection_start_time=date(1402, 10, 20),
            selection_end_time=date(1402, 11, 5),
            classes_start_time=date(1402, 11, 10),
            classes_end_time=date(1403, 3, 15),
            update_start_time=date(1402, 11, 6),
            update_end_time=date(1402, 11, 9),
            emergency_cancellation_end_time=date(1402, 11, 25),
            exams_start_time=date(1403, 3, 20),
            term_end_time=date(1403, 5, 13)
        )
        self.term.students.add(self.student)
        self.term.professors.add(self.professor)


        self.enrollment_verification = EnrollmentVerification.objects.create(
            student = self.student,
            enrollment_verification_file = "C:\Users\Asus\Desktop\verificationfile.pdf",
            term = self.term,
            issuance_certification_place = 'Tehran'

        )