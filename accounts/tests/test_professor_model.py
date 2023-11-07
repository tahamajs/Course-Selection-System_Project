from django.test import TestCase
from accounts.models import Professor, User, Professor, Expertise, Degree, FacultyUser
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
        self.degree2 = Degree.objects.create(name='لیسانس')
        self.professor = Professor.objects.create(user=self.faculty_user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)

    def test_professor_create(self):
        self.professor.save()
        self.assertEqual(self.professor.degree.name, 'دکترا')

    def test_professor_retrieve(self):
        professor = Professor.objects.get(pk=self.professor.pk)
        self.assertEqual(professor.degree.name, 'دکترا')

    def test_professor_update(self):
        old = self.professor.degree.name
        self.professor.degree = self.degree2
        self.professor.save()
        professor = Professor.objects.get(pk=self.professor.pk)
        self.assertNotEqual(professor.degree.name, old)

    def test_professor_delete(self):
        pk = self.professor.pk
        self.professor.delete()
        result = Professor.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
