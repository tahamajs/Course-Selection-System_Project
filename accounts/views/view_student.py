from rest_framework import viewsets
from accounts.models import Student
from accounts.serializers.serializer_student import StudentSerializerITAdmin
from accounts.permissions import IsITAdmin


class StudentViewSetITAdmin(viewsets.ModelViewSet):
    model = Student
    permission_classes = [IsITAdmin]
    serializer_class = StudentSerializerITAdmin



