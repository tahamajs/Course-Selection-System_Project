from django.test import TestCase
from accounts.models import User, ITAdmin, FacultyUser
from django.core.files.uploadedfile import SimpleUploadedFile


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.base_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.base_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )
        avatar = SimpleUploadedFile(name='test_image.jpg',
                                    content=open(r"D:\Gallery\My\king-head-vector-logo-icon_43623-454.jpg",
                                                 'rb').read(),
                                    content_type='image/jpeg')
        self.faculty_user = FacultyUser.objects.create(base_user=self.base_user, user_no=5214, avatar=avatar,
                                                       phone_number='+987654321', national_code='1547825478',
                                                       gender='M',
                                                       birth_date='1375-05-08')
        self.faculty_user2 = FacultyUser.objects.create(base_user=self.base_user2, user_no=8547, avatar=avatar,
                                                        phone_number='+985214785565', national_code='5247896551',
                                                        gender='F',
                                                        birth_date='1392-02-15')
        self.it_admin = ITAdmin.objects.create(user=self.faculty_user)

    def test_it_admin_create(self):
        self.it_admin.save()
        self.assertEqual(self.it_admin.user.base_user.username, 'testuser')
        self.assertEqual(self.it_admin.user.user_no, 5214)

    def test_it_admin_retrieve(self):
        it_admin = ITAdmin.objects.get(pk=self.it_admin.pk)
        self.assertEqual(it_admin.user.base_user.username, 'testuser')
        self.assertEqual(it_admin.user.user_no, 5214)

    def test_it_admin_update(self):
        old = self.it_admin.user
        self.it_admin.user = self.faculty_user2
        self.it_admin.save()
        it_admin = ITAdmin.objects.get(pk=self.it_admin.pk)
        self.assertNotEqual(it_admin.user, old)

    def test_it_admin_delete(self):
        pk = self.it_admin.pk
        self.it_admin.delete()
        result = ITAdmin.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
