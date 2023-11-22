from rest_framework import viewsets
from accounts.models.professor import Professor
from accounts.serializers import ProfessorSerializer
from accounts.permissions import IsITAdmin


class ProfessorViewSetITAdmin(viewsets.ModelViewSet):
    model = Professor
    permission_classes = [IsITAdmin]
    serializer_class = ProfessorSerializer



