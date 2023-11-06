from django.test import TestCase
from accounts.models import Expertise


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.expertise = Expertise.objects.create(name='نرم افزار')

    def test_it_admin_create(self):
        self.expertise.save()
        self.assertEqual(self.expertise.name, 'نرم افزار')

    def test_it_admin_retrieve(self):
        expertise = Expertise.objects.get(pk=self.expertise.pk)
        self.assertEqual(expertise.name, 'نرم افزار')

    def test_it_admin_update(self):
        old = self.expertise.name
        self.expertise.name = 'سخت افزار'
        self.expertise.save()
        name = Expertise.objects.get(pk=self.expertise.pk)
        self.assertNotEqual(name.name, old)

    def test_it_admin_delete(self):
        pk = self.expertise.pk
        self.expertise.delete()
        result = Expertise.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
