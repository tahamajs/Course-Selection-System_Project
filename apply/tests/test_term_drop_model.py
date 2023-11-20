from django.test import TestCase
from accounts.models import Student, User, Professor, Expertise, Degree
from college.models import FieldOfStudy, Faculty, Term
from apply.models.term_drop import TermDrop
from course.models.course import Course
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone


class TermDropModelTest(TestCase):
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

        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.user, entry_year='1375-10-10', entry_term=1, gpa=18.0,
                                              faculty=self.faculty, field_of_study=self.fos, supervisor=self.professor,
                                              military_service_status='SBJ',
                                              academic_years=2)
        self.student.courses_passed.add(*self.passed_courses)
        self.student.courses_taken.add(*self.taken_courses)

        # needs to be completed
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

        self.term_drop = TermDrop.objects.create(
            student=self.student,
            term=self.term,
            student_descr="student's description",
            educational_deputy_descr="Educational deputy's description",
        )

    def test_create_term_drop(self):
        self.term_drop.save()
        self.assertEqual(self.term_drop.student_descr, "student's description")

    def test_retrieve_term_drop(self):
        term_drop = TermDrop.objects.get(pk=self.term_drop.pk)
        self.assertEqual(term_drop.student_descr, "student's description")

    def test_update_term_drop(self):
        self.term_drop.student_descr = "New description"
        self.term_drop.save()
        self.assertEqual(self.term_drop.student_descr, "New description")

    def test_delete_term_drop(self):
        term_drop = TermDrop.objects.get(student_descr="student's description")
        term_drop.delete()
        self.assertEqual(TermDrop.objects.filter(student_descr="student's description").count(), 0)
