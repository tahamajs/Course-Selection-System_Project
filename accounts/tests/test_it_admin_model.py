from django.test import TestCase
from accounts.models import User, ITAdmin
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
                                    content=open(r"shared/files/avatar.jpg",
                                                 'rb').read(),
                                    content_type='image/jpeg')
        self.it_admin = ITAdmin.objects.create(user=self.base_user)

    def test_it_admin_create(self):
        self.it_admin.save()
        self.assertEqual(self.it_admin.user.username, 'testuser')


    def test_it_admin_retrieve(self):
        it_admin = ITAdmin.objects.get(pk=self.it_admin.pk)
        self.assertEqual(it_admin.user.username, 'testuser')


    def test_it_admin_update(self):
        old = self.it_admin.user
        self.it_admin.user = self.base_user2
        self.it_admin.save()
        it_admin = ITAdmin.objects.get(pk=self.it_admin.pk)
        self.assertNotEqual(it_admin.user, old)

    def test_it_admin_delete(self):
        pk = self.it_admin.pk
        self.it_admin.delete()
        result = ITAdmin.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
