from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from college.models import Faculty, FieldOfStudy, Term
from course.models import TermCourse, Course
from course.serializers import TermCourseSerializer
from course.permissions import IsEducationalDeputyOfTermCourseFaculty
from accounts.models import ITAdmin, User, Expertise, Degree, Professor, Student
from django.utils import timezone
from jdatetime import time


class TermCourseViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.it_admin = ITAdmin.objects.create(user=self.user)

        self.token = str(AccessToken.for_user(self.user))

        self.faculty = faculty = Faculty.objects.create(name='مهندسی کامپیوتر')
        self.course = Course.objects.create(name='مبانی کامپیوتر', faculty=faculty, credits=3, course_type='عمومی')
        self.field_of_study = FieldOfStudy.objects.create(
            name="Computer Science",
            group="Science",
            faculty=self.faculty,
            units=144,
            degree="master of science"
        )
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

        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.base_user, entry_year='1375-10-10', entry_term=1, gpa=18.0,
                                              faculty=self.faculty, field_of_study=self.fos, supervisor=self.professor,
                                              military_service_status='SBJ',
                                              academic_years=2)
        self.term = Term.objects.create(
            name="Spring Term",
            selection_start_time=timezone.datetime(1402, 10, 20),
            selection_end_time=timezone.datetime(1402, 11, 5),
            classes_start_time=timezone.datetime(1402, 11, 10),
            classes_end_time=timezone.datetime(1403, 3, 15),
            update_start_time=timezone.datetime(1402, 11, 6),
            update_end_time=timezone.datetime(1402, 11, 9),
            emergency_cancellation_end_time=timezone.datetime(1402, 11, 25),
            exams_start_time=timezone.datetime(1403, 3, 20),
            term_end_time=timezone.datetime(1403, 5, 13)
        )
        self.term.students.add(self.student)
        self.term.professors.add(self.professor)

        self.term_course = TermCourse.objects.create(course=self.course, term=self.term,
                                                     exam_date_time=timezone.datetime(1403, 3, 20),
                                                     exam_venue='دانشکده مهندسی کامپیوتر', professor=self.professor,
                                                     capacity=30, time=time(12, 11, 10), day=1)

    def test_term_course_list(self):
        url = '/course/term-courses/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_term_course(self):
        url = '/course/term-courses/'
        data = {
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_create_term_course(self):
        url = '/course/term-courses/'
        data = {
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_term_course_detail(self):
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_update_term_course(self):
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        data = {
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_update_term_course(self):
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        data = {
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_put_term_course(self):
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        data = {
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_put_term_course(self):
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        data = {
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        }
        response = self.client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_authenticated_user_can_delete_term_course(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        response  = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_user_cannot_delete_term_course(self):
        url = '/course/term-courses/' + str(self.term_course.id) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_term_course_serializer(self):
        serializer = TermCourseSerializer(instance=self.term_course)
        self.assertEqual(serializer.data['course'], self.course.id)
        self.assertEqual(serializer.data['term'], self.term.id)
        self.assertEqual(serializer.data['exam_date_time'], '1403-03-20T00:00:00+03:25:44')
        self.assertEqual(serializer.data['exam_venue'], 'دانشکده مهندسی کامپیوتر')
        self.assertEqual(serializer.data['professor'], self.professor.id)
        self.assertEqual(serializer.data['capacity'], 30)
        self.assertEqual(serializer.data['time'], '12:11:10')
        self.assertEqual(serializer.data['day'], 1)


    def test_term_course_serializer_create(self):
        serializer = TermCourseSerializer(data={
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        })
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(TermCourse.objects.count(), 2)

    def test_term_course_serializer_update(self):
        serializer = TermCourseSerializer(instance=self.term_course, data={
            "course": self.course.id,
            "term": self.term.id,
            "exam_date_time": "1403-01-01 12:00",
            "exam_venue": "دانشکده مهندسی کامپیوتر",
            "professor": self.professor.id,
            "capacity": 30,
            "time": "12:00",
            "day": 1
        })
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(TermCourse.objects.count(), 1)
        self.assertEqual(TermCourse.objects.first().exam_venue, 'دانشکده مهندسی کامپیوتر')
        self.assertEqual(TermCourse.objects.first().capacity, 30)
        self.assertEqual(TermCourse.objects.first().time, time(12, 0, 0))
        self.assertEqual(TermCourse.objects.first().day, 1)

    def test_term_course_serializer_delete(self):
        serializer = TermCourseSerializer(instance=self.term_course)
        self.assertEqual(TermCourse.objects.count(), 1)
        self.term_course.delete()
        self.assertEqual(TermCourse.objects.count(), 0)

