from django.test import TestCase
from accounts.models import Student, User, Professor, Expertise, Degree, FacultyUser
from college.models import Faculty, FieldOfStudy
from course.models import Course
from django.core.files.uploadedfile import SimpleUploadedFile


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.base_user = User.objects.create_user(
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
                                    content=open(r"shared/files/avatar.jpg",
                                                 'rb').read(),
                                    content_type='image/jpeg')
        self.faculty_user = FacultyUser.objects.create(base_user=self.base_user, user_no=5214, avatar=avatar,
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

    def test_student_create(self):
        self.student.save()
        self.assertEqual(self.student.gpa, 18.0)

    def test_student_retrieve(self):
        student = Student.objects.get(pk=self.student.pk)
        self.assertEqual(student.gpa, 18.0)

    def test_student_update(self):
        old = self.student.gpa
        self.student.gpa = 15.0
        self.student.save()
        student = Student.objects.get(pk=self.student.pk)
        self.assertNotEqual(student.gpa, old)

    def test_student_delete(self):
        pk = self.student.pk
        self.student.delete()
        result = Student.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
