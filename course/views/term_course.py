from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import TermCourse
from course.serializers import TermCourseSerializer

from accounts.permissions import IsITAdmin

from course.permissions import IsEducationalDeputyOfTermCourseFaculty


class TermCourseViewSet(viewsets.ModelViewSet):
    queryset = TermCourse.objects.all()
    serializer_class = TermCourseSerializer
    permission_classes = [IsAuthenticated, IsEducationalDeputyOfTermCourseFaculty | IsITAdmin, ]
