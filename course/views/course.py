from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from course.serializers import CourseSerializer
from accounts.permissions import IsITAdmin
from course.permissions import IsEducationalDeputyOfCourseFaculty


@extend_schema(tags=["Course"])
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsEducationalDeputyOfCourseFaculty | IsITAdmin, ]
    http_method_names = ['get', 'post', 'put', 'delete']
