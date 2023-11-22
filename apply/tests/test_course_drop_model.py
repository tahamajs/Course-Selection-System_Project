from django.test import TestCase
from accounts.models import Student, User, Professor, Expertise, Degree
from course.models.course import Course
from apply.models import CourseDrop
from college.models import FieldOfStudy, Faculty


class CourseDropModelTest(TestCase):
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
        

        self.course = Course.objects.create(
            name = 'physics2',
            faculty = self.faculty,
            credits = 3,
            course_type = 'elective',
        )

        pre_req1 = Course.objects.create(
        name='Pre-requisite Course 1',
        faculty=self.faculty,
        credits=3,
        course_type='core'
        )
        pre_req2 = Course.objects.create(
            name='Pre-requisite Course 2',
            faculty=self.faculty,
            credits=3,
            course_type='core'
        )

        co_req1 = Course.objects.create(
            name='Co-requisite Course 1',
            faculty=self.faculty,
            credits=3,
            course_type='core'
        )
        co_req2 = Course.objects.create(
            name='Co-requisite Course 2',
            faculty=self.faculty,
            credits=3,
            course_type='core'
        )

        self.course.pre_requisite.add(pre_req1, pre_req2)
        self.course.co_requisite.add(co_req1, co_req2)


        self.course_drop = CourseDrop.objects.create(
            student=self.student,
            course=self.course,
            student_description="Student's description",
            educational_deputy_description="Educational deputy's description",
        )

    def test_create_course_drop(self):
        self.course_drop.save()
        self.assertEqual(self.course_drop.student_description, "Student's description")

    def test_delete_course_drop(self):
        course_drop = CourseDrop.objects.create(
            student=self.student,
            course=self.course,
            student_description="Student's description",
            educational_deputy_description="Educational deputy's description",
        )

        course_drop_count_before = CourseDrop.objects.count()

        course_drop.delete()

        course_drop_count_after = CourseDrop.objects.count()
        self.assertEqual(course_drop_count_after, course_drop_count_before - 1)

    def test_retrieve_course_drop(self):
        retrieved_course_drop = CourseDrop.objects.get(pk=self.course_drop.pk)

        self.assertEqual(retrieved_course_drop.student, self.student)
        self.assertEqual(retrieved_course_drop.course, self.course)
        self.assertEqual(retrieved_course_drop.student_description, "Student's description")
        self.assertEqual(retrieved_course_drop.educational_deputy_description, "Educational deputy's description")

    def test_update_course_drop(self):
        course_drop = CourseDrop.objects.create(
            student=self.student,
            course=self.course,
            student_description="Student's description",
            educational_deputy_description="Educational deputy's description",
        )
        new_student_description = "Updated student's description"
        new_educational_deputy_description = "Updated educational deputy's description"
        course_drop.student_description = new_student_description
        course_drop.educational_deputy_description = new_educational_deputy_description
        course_drop.save()


        updated_course_drop = CourseDrop.objects.get(pk=course_drop.pk)


        self.assertEqual(updated_course_drop.student_description, new_student_description)
        self.assertEqual(updated_course_drop.educational_deputy_description, new_educational_deputy_description)