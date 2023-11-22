from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from accounts.models import Student
from accounts.serializers.serializer_student import StudentSerializerITAdmin
from accounts.permissions import IsITAdmin


@extend_schema(tags=["student"])
class StudentViewSetITAdmin(viewsets.ModelViewSet):
    model = Student
    permission_classes = [IsITAdmin]
    serializer_class = StudentSerializerITAdmin
    http_method_names = ['get', 'post', 'put', 'delete']
