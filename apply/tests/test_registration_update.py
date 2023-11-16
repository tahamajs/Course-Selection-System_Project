from django.test import TestCase
from django.utils import timezone

from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import Degree, Professor
from accounts.models.helper.expertise import Expertise
from accounts.models.user import User
from accounts.models.student import Student, FacultyUser
from college.models.faculty import Faculty
from college.models.fieldofstudy import FieldOfStudy
from apply.models.registration_update import RegistrationUpdate
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

        self.registration_update = RegistrationUpdate.objects.create(student=self.student)

        add_course1 = Course.objects.create(name='addcourse1', credits=1, faculty=self.faculty)
        add_course2 = Course.objects.create(name='addcourse2', credits=2, faculty=self.faculty)

        del_course1 = Course.objects.create(name='delcourse1', credits=1, faculty=self.faculty)
        del_course2 = Course.objects.create(name='delcourse2', credits=2, faculty=self.faculty)

        self.registration_update.add_courses.add(add_course1, add_course2)
        self.registration_update.del_courses.add(del_course1, del_course2)

    def test_create_registration_update(self):
        # Check if registration_update created successfully
        self.assertEqual(self.registration_update.student.user.base_user.username, 'testuser')

        add_courses = list(self.registration_update.add_courses.all())
        add_courses_list = [course.name for course in add_courses]
        self.assertEqual(add_courses_list, ['addcourse1', 'addcourse2'])

        del_courses = list(self.registration_update.del_courses.all())
        del_courses_list = [course.name for course in del_courses]
        self.assertEqual(del_courses_list, ['delcourse1', 'delcourse2'])

        self.assertFalse(self.registration_update.approval_status)

    def test_retrieve_registration_update(self):
        # Check if registration_update retrieved successfully
        retrieved_registration_update = RegistrationUpdate.objects.get(pk=self.registration_update.pk)

        self.assertEqual(retrieved_registration_update.student.user.base_user.username, 'testuser')

        retrieved_add_courses = list(retrieved_registration_update.add_courses.all())
        retrieved_add_courses_list = [course.name for course in retrieved_add_courses]
        self.assertEqual(retrieved_add_courses_list, ['addcourse1', 'addcourse2'])

        retrieved_del_courses = list(retrieved_registration_update.del_courses.all())
        retrieved_del_courses_list = [course.name for course in retrieved_del_courses]
        self.assertEqual(retrieved_del_courses_list, ['delcourse1', 'delcourse2'])

        self.assertFalse(retrieved_registration_update.approval_status)

    def test_update_registration_update(self):
        self.registration_update.add_courses.clear()
        self.registration_update.del_courses.clear()

        add_course1_update = Course.objects.create(name='addcourse1update', credits=2, faculty=self.faculty)
        add_course2_update = Course.objects.create(name='addcourse2update', credits=3, faculty=self.faculty)
        self.registration_update.add_courses.add(add_course1_update, add_course2_update)

        del_course1_update = Course.objects.create(name='delcourse1update', credits=3, faculty=self.faculty)
        del_course2_update = Course.objects.create(name='delcourse2update', credits=4, faculty=self.faculty)
        self.registration_update.del_courses.add(del_course1_update, del_course2_update)

        self.registration_update.approval_status = True
        self.assertTrue(self.registration_update.approval_status)

    def test_delete_registration_update(self):
        pk = self.registration_update.pk
        RegistrationUpdate.objects.filter(pk=pk).delete()
        with self.assertRaises(RegistrationUpdate.DoesNotExist):
            RegistrationUpdate.objects.get(pk=pk)









