from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import  Professor, Expertise, Degree , EducationalDeputy
from accounts.models import User

from college.models import Faculty, FieldOfStudy
from course.models import Course



class UserFactory:
    pass


class ProfessorViewSetTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = UserFactory(username='testuser', password='testpassword')

        # Create an educational deputy and faculty
        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                               degree='کارشناسی')
        self.educational_deputy = EducationalDeputy.objects.create(user=self.base_user, faculty=self.faculty,
                                                                   field_of_study=self.fos)
        self.educational_faculty = self.educational_deputy.faculty

        # Create a professor in the same faculty as the educational deputy
        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.passed_courses = [Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                     credits=3, course_type='core'), ]
        self.taken_courses = [Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                    credits=3, course_type='specialized'), ]


        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.degree2 = Degree.objects.create(name='لیسانس')
        self.professor = Professor.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        # Generate a JWT token for the user
        self.token = str(AccessToken.for_user(self.user))

        self.client = APIClient()



