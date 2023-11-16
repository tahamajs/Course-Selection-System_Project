from django.test import TestCase
from django.utils import timezone

from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import Degree, Professor
from accounts.models.helper.expertise import Expertise
from accounts.models.user import User
from accounts.models.student import Student, FacultyUser
from college.models.faculty import Faculty
from college.models.fieldofstudy import FieldOfStudy
from apply.models.registration import Registration
from course.models.course import Course


class RegistrationModelTestCase(TestCase):
    def setUp(self) -> None:
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

        avatar = SimpleUploadedFile(name='default.jpg',
                                    content=open(r"shared/files/avatar.jpg",
                                                 'rb').read(),
                                    content_type='image/jpeg')
        self.faculty_user = FacultyUser.objects.create(base_user=self.user, user_no=1521, avatar=avatar,
                                                       phone_number='+987654321', national_code='1547825478',
                                                       gender='M',
                                                       birth_date=timezone.datetime(1375, 5, 8))
        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.faculty_user, faculty=self.faculty,
                                                  field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.faculty_user, entry_year=timezone.datetime(1375, 10, 10), entry_term=1,
                                              gpa=18.0,
                                              faculty=self.faculty, field_of_study=self.fos,
                                              supervisor=self.professor,
                                              military_service_status='SBJ',
                                              academic_years=2)
        self.student.courses_passed.add(*self.passed_courses)
        self.student.courses_taken.add(*self.taken_courses)

        self.registration = Registration.objects.create(student=self.student)

        course1 = Course.objects.create(name='testcourse1', credits=1, faculty=self.faculty)
        course2 = Course.objects.create(name='testcourse2', credits=2, faculty=self.faculty)
        self.registration.courses.add(course1, course2)

    def test_create_registration(self):
        # Check if registration created successfully
        self.assertEqual(self.registration.student.user.base_user.username, 'testuser')

        courses = list(self.registration.courses.all())
        courses_list = [course.name for course in courses]
        self.assertEqual(courses_list, ['testcourse1', 'testcourse2'])

        self.assertFalse(self.registration.approval_status)

    def test_retrieve_registration(self):
        # Check if registration retrieved successfully
        retrieved_registration = Registration.objects.get(pk=self.registration.pk)

        self.assertEqual(retrieved_registration.student.user.base_user.username, 'testuser')

        retrieved_courses = list(retrieved_registration.courses.all())
        retrieved_courses_list = [course.name for course in retrieved_courses]
        self.assertEqual(retrieved_courses_list, ['testcourse1', 'testcourse2'])

        self.assertFalse(retrieved_registration.approval_status)

    def test_update_registration(self):
        # Check if registration updated successfully
        self.registration.courses.clear()
        course1_update = Course.objects.create(name='updatecourse1', credits=3, faculty=self.faculty)
        course2_update = Course.objects.create(name='updatecourse2', credits=4, faculty=self.faculty)
        self.registration.courses.add(course1_update, course2_update)
        updated_courses = list(self.registration.courses.all())
        updated_courses_list = [course.name for course in updated_courses]
        self.assertEqual(updated_courses_list, ['updatecourse1', 'updatecourse2'])

        self.registration.approval_status = True
        self.assertTrue(self.registration.approval_status)

    def test_delete_registration(self):
        # Check if registration deleted successfully
        pk = self.registration.pk
        Registration.objects.filter(pk=pk).delete()
        with self.assertRaises(Registration.DoesNotExist):
            Registration.objects.get(pk=pk)
