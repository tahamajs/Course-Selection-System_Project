import pytz
from django.test import TestCase

from accounts.models import Student, Professor, User, Degree
from accounts.models.helper.expertise import Expertise
from course.models import StudentCourse, Course, TermCourse
from college.models import Term, Faculty, FieldOfStudy
from jdatetime import time
from django.utils import timezone


class CourseModelTest(TestCase):
    def setUp(self):
        self.faculty = faculty = Faculty.objects.create(name='مهندسی کامپیوتر')
        Course.objects.create(name='مبانی کامپیوتر', faculty=faculty, credits=3, course_type='عمومی')

    def test_course_creation(self):
        course = Course.objects.get(name='مبانی کامپیوتر')
        self.assertEqual(course.name, 'مبانی کامپیوتر')
        self.assertEqual(course.faculty.name, 'مهندسی کامپیوتر')

    def test_course_str(self):
        course = Course.objects.get(name='مبانی کامپیوتر')
        self.assertEqual(course.__str__(), 'مبانی کامپیوتر')

    def test_delete_course(self):
        new_course = Course.objects.create(name='برنامه نویسی پیشرفته', faculty=self.faculty, credits=3,
                                           course_type='عمومی')
        new_course.delete()
        self.assertEqual(Course.objects.count(), 1)

    def test_update_course(self):
        course = Course.objects.get(name='مبانی کامپیوتر')
        course.name = 'مبانی کامپیوتر 2'
        course.save()
        self.assertEqual(course.name, 'مبانی کامپیوتر 2')

    def test_course_type(self):
        course = Course.objects.get(name='مبانی کامپیوتر')
        self.assertEqual(course.course_type, 'عمومی')

    def test_course_credits(self):
        course = Course.objects.get(name='مبانی کامپیوتر')
        self.assertEqual(course.credits, 3)

    def test_course_faculty(self):
        course = Course.objects.get(name='مبانی کامپیوتر')
        self.assertEqual(course.faculty.name, 'مهندسی کامپیوتر')


#

class StudentCourseTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='مبانی کامپیوتر',
                                            faculty=Faculty.objects.create(name='مهندسی کامپیوتر'), credits=3,
                                            course_type='عمومی')
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
        self.student_course = StudentCourse.objects.create(course=self.course, course_state='passed', grade=20,
                                                           term=self.term)

    def test_student_course_course(self):
        self.assertEqual(self.student_course.course.name, "مبانی کامپیوتر")
        self.assertEqual(self.student_course.course.faculty.name, "مهندسی کامپیوتر")

    def test_student_course_course_state(self):
        self.assertEqual(self.student_course.course_state, "passed")

    def test_student_course_grade(self):
        self.assertEqual(self.student_course.grade, 20)

    def test_student_course_term(self):
        self.assertEqual(self.student_course.term.name, "Spring Term")

    def test_student_course_str(self):
        self.assertEqual(self.student_course.__str__(), "مبانی کامپیوتر - Spring Term")

    def test_delete_student_course(self):
        self.student_course.delete()
        self.assertEqual(StudentCourse.objects.count(), 0)

    def test_update_student_course(self):
        self.student_course.grade = 19
        self.student_course.save()
        self.assertEqual(self.student_course.grade, 19)

    def test_student_course_course_type(self):
        self.assertEqual(self.student_course.course.course_type, "عمومی")

    def test_student_course_course_credits(self):
        self.assertEqual(self.student_course.course.credits, 3)

    def test_student_course_course_faculty(self):
        self.assertEqual(self.student_course.course.faculty.name, "مهندسی کامپیوتر")


class TermCourseTest(TestCase):
    def setUp(self):
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

    def test_term_name(self):
        self.assertEqual(self.term.name, "Spring Term")

    def test_course(self):
        self.assertEqual(self.term_course.course.name, "مبانی کامپیوتر")
        self.assertEqual(self.term_course.course.faculty.name, "مهندسی کامپیوتر")

    def test_capacity(self):
        self.assertEqual(self.term_course.capacity, 30)

    def test_time(self):
        self.assertEqual(self.term_course.time, time(12, 11, 10))

    def test_day(self):
        self.assertEqual(self.term_course.day, 1)

    def test_term_str(self):
        self.assertEqual(self.term_course.__str__(), "مبانی کامپیوتر - Spring Term")

    def test_exam_date_time(self):
        self.assertEqual(self.term_course.exam_date_time, timezone.datetime(1403, 3, 20))

    def test_exam_venue(self):
        self.assertEqual(self.term_course.exam_venue, "دانشکده مهندسی کامپیوتر")

    def test_professor(self):
        self.assertEqual(self.term_course.professor.user.username, "testuser")

    def test_term(self):
        self.assertEqual(self.term_course.term.name, "Spring Term")
        self.assertEqual(self.term_course.term.students.first().user.username, "testuser")
        self.assertEqual(self.term_course.term.professors.first().user.username, "testuser")

    def test_delete_term_course(self):
        self.term_course.delete()
        self.assertEqual(TermCourse.objects.count(), 0)

    def test_update_term_course(self):
        self.term_course.capacity = 50
        self.term_course.save()
        self.assertEqual(self.term_course.capacity, 50)

    def test_term_course_str(self):
        self.assertEqual(self.term_course.__str__(), "مبانی کامپیوتر - Spring Term")
