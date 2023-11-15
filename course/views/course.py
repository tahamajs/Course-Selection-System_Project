from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from course.serializers import CourseSerializer

from accounts.permissions import IsEducationalDeputy, IsITAdmin


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsEducationalDeputy | IsITAdmin, ]
