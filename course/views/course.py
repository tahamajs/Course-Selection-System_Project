from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from course.models import Course
from course.models.student_course import StudentCourse
from course.models.term_course import TermCourse
from course.serializers import CourseSerializer
from accounts.permissions import IsITAdmin
from course.permissions import IsEducationalDeputyOfCourseFaculty
from course.serializers.student_course import StudentCourseSerializer
from course.serializers.term_course import TermCourseSerializer


@extend_schema(tags=["Course"])
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsEducationalDeputyOfCourseFaculty | IsITAdmin, ]
    http_method_names = ['get', 'post', 'put', 'delete']

    @action(detail=True, methods=['get'], url_path='class-schedule')
    def get_class_schedule(self, request, pk=None):
        try:
            student_courses = StudentCourse.objects.filter(student=pk)
            serializer = StudentCourseSerializer(student_courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'], url_path='exam-schedule')
    def get_exam_schedule(self, request, pk=None):
        try:
            term_courses = TermCourse.objects.filter(term__students=pk)
            serializer = TermCourseSerializer(term_courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
