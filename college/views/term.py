from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from college.models import Term
from course.models import Course
from college.serializers import TermSerializer
from course.serializers import CourseSerializer
from accounts.models import Student, ITAdmin
from accounts.permissions import IsStudent, IsProfessor, IsITAdmin


@extend_schema(tags=["term"])
class TermViewSet(viewsets.ModelViewSet):
    permission_classes = [IsITAdmin, IsAuthenticated]
    queryset = Term.objects.all()
    serializer_class = TermSerializer

    def perform_create(self, serializer):
        serializer.save()


@extend_schema(tags=["term"])
class TermListAPIView(generics.ListAPIView):
    permission_classes = (IsStudent | IsProfessor,)
    queryset = Term.objects.all()
    serializer_class = TermSerializer


@extend_schema(tags=["term"])
class TermDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsStudent | IsProfessor,)
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    lookup_field = 'pk'


@extend_schema(tags=["term"])
class StudentCoursesAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = (IsStudent | IsProfessor,)

    def get_queryset(self):

        student_id = self.kwargs['pk']

        if student_id == 'me':
            user = self.request.user

            if hasattr(user, 'student_user'):
                student = user.student

            else:
                return Course.objects.none()
        else:
            try:

                student = Student.objects.get(id=int(student_id))

            except Student.DoesNotExist:
                return Course.objects.none()

        course_token = student.courses_taken.all()
        available_courses = Course.objects.exclude(id__in=course_token, faculty_id=student.faculty_id)

        course_with_pre_requisite = available_courses.filter(pre_requisite__in=course_token)
        course_with_co_requisite = available_courses.filter(co_requisite__in=course_token)
        queryset = course_with_pre_requisite.union(course_with_co_requisite)
        return queryset
