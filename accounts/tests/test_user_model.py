from django.test import TestCase
from accounts.models import User


class UserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_user_create(self):
        self.user.save()
        self.assertEqual(self.user.username, 'testuser')

    def test_user_retrieve(self):
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.username, 'testuser')

    def test_user_update(self):
        old = self.user.username
        self.user.username = 'testuser2'
        self.user.save()
        user = User.objects.get(pk=self.user.pk)
        self.assertNotEqual(user.username, old)

    def test_user_delete(self):
        pk = self.user.pk
        self.user.delete()
        result = User.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
