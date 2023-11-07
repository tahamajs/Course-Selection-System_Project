from django.test import TestCase
from college.models import Faculty, FieldOfStudy, Term
from django.core.files.uploadedfile import SimpleUploadedFile
from course.models import Course
from accounts.models import Student, User, Professor, Expertise, Degree, FacultyUser
from django.utils import timezone
import pytz


class FacultyModelTest(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name="Engineering Faculty")

    def test_create_faculty(self):
        self.faculty.save()
        self.assertEqual(Faculty.objects.count(), 1)

    def test_read_faculty(self):
        faculty = Faculty.objects.get(name="Engineering Faculty")
        self.assertEqual(faculty.name, "Engineering Faculty")

    def test_update_faculty(self):
        faculty = Faculty.objects.get(name="Engineering Faculty")
        faculty.name = "Faculty of Technology"
        faculty.save()
        updated_faculty = Faculty.objects.get(name="Faculty of Technology")
        self.assertEqual(updated_faculty.name, "Faculty of Technology")

    def test_delete_faculty(self):
        faculty = Faculty.objects.get(name="Engineering Faculty")
        faculty.delete()
        self.assertEqual(Faculty.objects.filter(name="Engineering Faculty").count(), 0)


class FieldOfStudyModelTest(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name="Science Faculty")
        self.field_of_study = FieldOfStudy.objects.create(
            name="Computer Science",
            group="Science",
            faculty=self.faculty,
            units=144,
            degree="master of science"
        )

    def test_create_field_of_study(self):
        self.field_of_study.save()
        self.assertEqual(FieldOfStudy.objects.count(), 1)

    def test_read_field_of_study(self):
        field_of_study = FieldOfStudy.objects.get(name="Computer Science")
        self.assertEqual(field_of_study.name, "Computer Science")

    def test_update_field_of_study(self):
        field_of_study = FieldOfStudy.objects.get(name="Computer Science")
        field_of_study.name = "CS"
        field_of_study.save()

        updated_field_of_study = FieldOfStudy.objects.get(name="CS")
        self.assertEqual(updated_field_of_study.name, "CS")

    def test_delete_field_of_study(self):
        field_of_study = FieldOfStudy.objects.get(name="Computer Science")
        field_of_study.delete()
        self.assertEqual(FieldOfStudy.objects.filter(name="Computer Science").count(), 0)


class TermModelTest(TestCase):
    def setUp(self):
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
                                    content_type='image/png')
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

    def test_create_term(self):
        self.term.save()
        self.assertEqual(Term.objects.count(), 1)

    def test_read_term(self):
        term = Term.objects.get(name="Spring Term")
        self.assertEqual(term.name, "Spring Term")

    def test_update_term(self):
        term = Term.objects.get(name="Spring Term")
        term.name = "Fall Term"
        term.save()

        updated_term = Term.objects.get(name="Fall Term")
        self.assertEqual(updated_term.name, "Fall Term")

    def test_delete_term(self):
        term = Term.objects.get(name="Spring Term")
        term.delete()
        self.assertEqual(Term.objects.filter(name="Spring Term").count(), 0)

    def test_term_end_time(self):
        term = Term.objects.get(name="Spring Term")
        self.assertEqual(term.term_end_time, timezone.datetime(1403, 5, 13))
