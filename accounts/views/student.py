from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.models import EducationalDeputy
from accounts.models.student import Student
from accounts.serializers import StudentSerializer, StudentSerializerAllFields
from accounts.permissions import EducationalDeputyOrStudentOrProfessorPermission


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [EducationalDeputyOrStudentOrProfessorPermission]
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.action == 'update':
            return self.serializer_class
        elif self.action == 'retrieve' or self.action == 'list':
            return StudentSerializerAllFields
        else:
            return self.serializer_class

    def retrieve(self, request, pk=None):
        educational_faculty = EducationalDeputy.objects.get(user=self.request.user).faculty
        if pk:
            student = get_object_or_404(Student, pk=pk)
            if student.faculty == educational_faculty:
                serializer = self.get_serializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'you cant access student with different faculty'},
                                status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if EducationalDeputy.objects.filter(user=self.request.user).exists():
            educational_faculty = EducationalDeputy.objects.get(user=self.request.user).faculty
            return Student.objects.filter(faculty=educational_faculty)
        return Student.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
