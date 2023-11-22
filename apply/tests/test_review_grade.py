from django.test import TestCase
from django.utils import timezone
from accounts.models import Degree, Professor
from accounts.models.helper.expertise import Expertise
from django.contrib.auth import get_user_model
from accounts.models.student import Student
from college.models.faculty import Faculty
from college.models.fieldofstudy import FieldOfStudy
from course.models.course import Course
from apply.models.review_grade import ReviewGrade

User = get_user_model()


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


        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.user, faculty=self.faculty,
                                                  field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.user, entry_year=timezone.datetime(1375, 10, 10),
                                              entry_term=1,
                                              gpa=18.0,
                                              faculty=self.faculty, field_of_study=self.fos,
                                              supervisor=self.professor,
                                              military_service_status='SBJ',
                                              academic_years=2)
        self.student.courses_passed.add(*self.passed_courses)
        self.student.courses_taken.add(*self.taken_courses)

        self.courses_taken_list = list(self.student.courses_taken.all())

        self.review_grade = ReviewGrade.objects.create(student=self.student, course=self.courses_taken_list[0],
                                                       review_text='testreview', result_text='testresult')

    def test_create_review_grade(self):
        # Check if review_grade created successfully
        self.assertEqual(self.review_grade.student.user.username, 'testuser')
        self.assertEqual(self.review_grade.course.name, 'سیستم عامل')

    def test_retrieve_review_grade(self):
        # Check if review_grade retrieved successfully
        retrieved_review_grade = ReviewGrade.objects.get(pk=self.review_grade.pk)
        self.assertEqual(retrieved_review_grade.student.user.username, 'testuser')
        self.assertEqual(retrieved_review_grade.course.name, 'سیستم عامل')
        self.assertEqual(retrieved_review_grade.review_text, 'testreview')
        self.assertEqual(retrieved_review_grade.result_text, 'testresult')

    def test_update_review_grade(self):
        self.review_grade.course.name = 'testcourse'
        self.assertEqual(self.review_grade.course.name, 'testcourse')

        self.review_grade.review_text = 'testreviewupdate'
        self.assertEqual(self.review_grade.review_text, 'testreviewupdate')

        self.review_grade.result_text = 'testresultupdate'
        self.assertEqual(self.review_grade.result_text, 'testresultupdate')

    def test_delete_review_grade(self):
        pk = self.review_grade.pk
        ReviewGrade.objects.filter(pk=pk).delete()
        with self.assertRaises(ReviewGrade.DoesNotExist):
            ReviewGrade.objects.get(pk=pk)
