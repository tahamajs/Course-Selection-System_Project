from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from apply.models import RegistrationUpdate
from accounts.models import ITAdmin, User, Expertise, Degree, Professor, Student
from college.models import Faculty, FieldOfStudy
from course.models import Course
from django.utils import timezone


class RegistrationUpdateViewSetTests(APITestCase):
    def setUp(self):
        self.base_user = User.objects.create_user(username='base_user', password='password')
        self.IT_admin_user = ITAdmin.objects.create(user=self.base_user)
        self.IT_admin_token = str(AccessToken.for_user(self.IT_admin_user))
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

        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.user, faculty=self.faculty,
                                                  field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.user, entry_year=timezone.datetime(1375, 10, 10), entry_term=1,
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

    def test_authentication_create_list(self):
        url = '/apply/registration-update/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.IT_admin_token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_retrieve_update_partial_update_destroy(self):
        url = '/apply/registration-update/1/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.IT_admin_token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_authentication_create_list(self):
    #
    #     url = '/apply/registration-update/'
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.IT_admin_token)
    #     self.user2 = User.objects.create_user( username='testuser2', password='testpassword')
    #     self.fos2 = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,degree='کارشناسی')
    #     self.faculty2 = Faculty.objects.create(name='فنی حرفه ای 2 تبریز')
    #     self.student1 = Student.objects.create(user=self.user2, entry_year=timezone.datetime(1375, 10, 10), entry_term=1 , gpa=18.0,academic_years=2,faculty=self.faculty2, field_of_study=self.fos2, supervisor=self.professor, military_service_status='SBJ')
    #     data = {
    #         'student': self.student1.id,
    #         'add_courses': [course.id for course in self.passed_courses],
    #         'del_courses': [course.id for course in self.taken_courses],
    #         'approval_status': 'E'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_retrieve_update_partial_update_destroy(self):
        # Create a new registration update for testing
        new_registration_update = RegistrationUpdate.objects.create(student=self.student)

        url = f'/apply/registration-update/{new_registration_update.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.IT_admin_token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = {
            'add_courses': [course.id for course in self.passed_courses],
            'del_courses': [course.id for course in self.taken_courses],
            'approval_status': 'P'
        }
        response = self.client.put(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        partial_data = {'approval_status': 'A'}
        response = self.client.patch(url, partial_data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
