from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from course.models import TermCourse
from course.serializers import TermCourseSerializer
from accounts.permissions import IsITAdmin
from course.permissions import IsEducationalDeputyOfTermCourseFaculty


@extend_schema(tags=["TermCourse"])
class TermCourseViewSet(viewsets.ModelViewSet):
    queryset = TermCourse.objects.all()
    serializer_class = TermCourseSerializer
    permission_classes = [IsAuthenticated, IsEducationalDeputyOfTermCourseFaculty | IsITAdmin, ]
    http_method_names = ['get', 'put', 'delete']
