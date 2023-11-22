# from django.test import TestCase
# from accounts.models import Student, User, Professor, Expertise, Degree, FacultyUser
# from college.models import Faculty, FieldOfStudy
# from course.models import Course
# from django.core.files.uploadedfile import SimpleUploadedFile
#
#
# class CustomUserModelTest(TestCase):
#
#     def setUp(self):
#         # Create a test user
#         self.base_user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )
#         avatar = SimpleUploadedFile(name='test_image.jpg',
#                                     content=open(r"shared/files/avatar.jpg",
#                                                  'rb').read(),
#                                     content_type='image/jpeg')
#         self.faculty_user = FacultyUser.objects.create(base_user=self.base_user, user_no=5214, avatar=avatar,
#                                                        phone_number='+987654321', national_code='1547825478',
#                                                        gender='M',
#                                                        birth_date='1375-05-08')
#
#     def test_faculty_user_create(self):
#         self.faculty_user.save()
#         self.assertEqual(self.faculty_user.user_no, 5214)
#
#     def test_faculty_user_retrieve(self):
#         faculty_user = FacultyUser.objects.get(pk=self.faculty_user.pk)
#         self.assertEqual(faculty_user.user_no, 5214)
#
#     def test_faculty_user_update(self):
#         old = self.faculty_user.user_no
#         self.faculty_user.user_no = 6541
#         self.faculty_user.save()
#         faculty_user = FacultyUser.objects.get(pk=self.faculty_user.pk)
#         self.assertNotEqual(faculty_user.user_no, old)
#
#     def test_faculty_user_delete(self):
#         pk = self.faculty_user.pk
#         self.faculty_user.delete()
#         result = FacultyUser.objects.filter(pk=pk).exists()
#         self.assertEqual(result, False)
