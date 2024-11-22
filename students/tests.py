from rest_framework.test import APITestCase
from rest_framework import status
from .models import Student

class StudentAPITests(APITestCase):
    def setUp(self):
        self.student_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "dob": "2000-01-01",
        }
        self.student = Student.objects.create(**self.student_data)

    def test_get_student_list(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_student(self):
        response = self.client.post('/students/', self.student_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
