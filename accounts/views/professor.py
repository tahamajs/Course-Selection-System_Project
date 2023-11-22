from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.models import EducationalDeputy
from accounts.models.professor import Professor
from accounts.serializers import ProfessorSerializer, ProfessorSerializerAllFields
from accounts.permissions import EducationalDeputyOrStudentOrProfessorPermission


@extend_schema(tags=["professor"])
class ProfessorViewSet(viewsets.ModelViewSet):
    permission_classes = [EducationalDeputyOrStudentOrProfessorPermission, IsAuthenticated]
    serializer_class = ProfessorSerializer
    http_method_names = ['get', 'put']

    def get_serializer_class(self):
        if self.action == 'update':
            return self.serializer_class
        elif self.action == 'retrieve' or self.action == 'list':
            return ProfessorSerializerAllFields
        else:
            return self.serializer_class

    def retrieve(self, request, pk=None):
        educational_faculty = EducationalDeputy.objects.get(user=self.request.user).faculty
        if pk:
            professor = get_object_or_404(Professor, pk=pk)
            if professor.faculty == educational_faculty:
                serializer = self.get_serializer(professor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'you cant access professor with different faculty'},
                                status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if EducationalDeputy.objects.filter(user=self.request.user).exists():
            educational_faculty = EducationalDeputy.objects.get(user=self.request.user).faculty
            return Professor.objects.filter(faculty=educational_faculty).order_by('pk')
        return Professor.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
