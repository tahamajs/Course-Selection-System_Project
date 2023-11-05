from django.test import TestCase
from accounts.models import Student, User, Professor, Expertise, Degree, FacultyUser
from course.models.course import Course
from requests.models import CourseDrop
from college.models import FieldOfStudy, Faculty
from django.core.files.uploadedfile import SimpleUploadedFile




class CourseDropTestCase(TestCase):
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

        avatar = SimpleUploadedFile(name='test_image.jpg',
                                    content=open(r"D:\Gallery\My\king-head-vector-logo-icon_43623-454.jpg",
                                                 'rb').read(),
                                    content_type='image/jpeg')
        self.faculty_user = FacultyUser.objects.create(base_user=self.user, user_no=5214, avatar=avatar,
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

            # Create a CourseDrop instance
        self.course_drop = CourseDrop.objects.create(
            student=self.student,
            course=self.course,
            student_description="Student's description",
            educational_deputy_description="Educational deputy's description",
        )

    def test_course_drop_attributes(self):
        self.assertEqual(self.course_drop.student, self.student)
        self.assertEqual(self.course_drop.course, self.course)
        self.assertEqual(self.course_drop.student_description, "Student's description")
        self.assertEqual(self.course_drop.educational_deputy_description, "Educational deputy's description")

    def test_related_names(self):
        self.assertEqual(self.course_drop.student.course_drop_req_student.all().count(), 1)
        self.assertEqual(self.course_drop.course.course_drop_req_course.all().count(), 1)
