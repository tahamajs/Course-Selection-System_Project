from django.test import TestCase
from accounts.models import User


class UserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_user(self):
        # Check if the user is created successfully
        self.assertEqual(self.user.username, 'testuser')
