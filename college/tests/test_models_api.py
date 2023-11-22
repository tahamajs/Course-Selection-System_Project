from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import User
from college.models import Faculty
from college.serializers import FacultySerializer
from accounts.models import ITAdmin

class FacultyViewSetTests(APITestCase):
    def setUp(self):
        self.base_user = User.objects.create_user(username='base_user', password='password')
        self.IT_admin_user = ITAdmin.objects.create(user = self.base_user)
        self.IT_admin_token = str(AccessToken.for_user(self.IT_admin_user))

        self.faculty = Faculty.objects.create(name="Engineering Faculty")


    def test_authentication_list_faculty(self):
        url = '/college/faculty/'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.IT_admin_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        print('  '.join(response.data['results'][0] ))
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'] , self.faculty.name)

    def test_authentication_create_faculty(self):
        url = '/college/faculty/'
        data = {'name': 'Science Faculty'}
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {self.IT_admin_token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Faculty.objects.count(), 2)
        self.assertEqual(Faculty.objects.get(id=2).name, 'Science Faculty')

    def test_authentication_retrieve_faculty(self):
        url = '/college/faculty/1/'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.IT_admin_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.faculty.name)

    def test_authentication_update_faculty(self):
        url = '/college/faculty/1/'
        data = {'name': 'Science Faculty'}
        response = self.client.put(url, data, HTTP_AUTHORIZATION=f'Bearer {self.IT_admin_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Faculty.objects.get(id=1).name, 'Science Faculty')

    def test_authentication_delete_faculty(self):
        url = '/college/faculty/1/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Bearer {self.IT_admin_token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Faculty.objects.count(), 0)

    def test_authentication_put_faculty(self):
        url = '/college/faculty/1/'
        data = {'name': 'Science Faculty'}
        response = self.client.put(url, data, HTTP_AUTHORIZATION=f'Bearer {self.IT_admin_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Faculty.objects.get(id=1).name, 'Science Faculty')
