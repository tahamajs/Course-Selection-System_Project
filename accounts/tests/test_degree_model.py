from django.test import TestCase
from accounts.models import Degree


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.degree = Degree.objects.create(name='دکترا')

    def test_it_admin_create(self):
        self.degree.save()
        self.assertEqual(self.degree.name, 'دکترا')

    def test_it_admin_retrieve(self):
        degree = Degree.objects.get(pk=self.degree.pk)
        self.assertEqual(degree.name, 'دکترا')

    def test_it_admin_update(self):
        old = self.degree.name
        self.degree.name = 'لیسانس'
        self.degree.save()
        name = Degree.objects.get(pk=self.degree.pk)
        self.assertNotEqual(name.name, old)

    def test_it_admin_delete(self):
        pk = self.degree.pk
        self.degree.delete()
        result = Degree.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
#