from django.test import TestCase
from datetime import datetime, date
from college.models import Faculty, FieldOfStudy, Term
from accounts.models import Student, Professor


class FacultyModelTest(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name="Engineering Faculty")

    def test_faculty_name(self):
        faculty = Faculty.objects.get(name="Engineering Faculty")
        self.assertEqual(faculty.name, "Engineering Faculty")


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

    def test_field_of_study_name(self):
        field_of_study = FieldOfStudy.objects.get(name="Computer Science")
        self.assertEqual(field_of_study.name, "Computer Science")

    def test_field_of_study_degree(self):
        field_of_study = FieldOfStudy.objects.get(name="Computer Science")
        self.assertEqual(field_of_study.degree, "master of science")

    def test_field_of_study_associated_faculty(self):
        field_of_study = FieldOfStudy.objects.get(name="Computer Science")
        self.assertEqual(field_of_study.faculty.name, "Science Faculty")


class TermModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="Ahmad")
        self.professor = Professor.objects.create(name="Dr javadi")
        self.term = Term.objects.create(
            name="Spring Term",
            selection_start_time=datetime(2023, 1, 1),
            selection_end_time=datetime(2023, 1, 15),
            classes_start_time=datetime(2023, 2, 1),
            classes_end_time=datetime(2023, 5, 31),
            update_start_time=datetime(2023, 1, 16),
            update_end_time=datetime(2023, 1, 31),
            emergency_cancellation_end_time=datetime(2023, 2, 15),
            exams_start_time=date(2023, 6, 1),
            term_end_time=date(2023, 6, 15)
        )
        self.term.students.add(self.student)
        self.term.professors.add(self.professor)

    def test_term_name(self):
        term = Term.objects.get(name="Spring Term")
        self.assertEqual(term.name, "Spring Term")

    def test_term_students(self):
        term = Term.objects.get(name="Spring Term")
        self.assertEqual(term.students.first().name, "Ahmad")

    def test_term_professors(self):
        term = Term.objects.get(name="Spring Term")
        self.assertEqual(term.professors.first().name, "Dr javadi")

    def test_term_end_time(self):
        term = Term.objects.get(name="Spring Term")
        self.assertEqual(term.term_end_time, date(2023, 6, 15))
