from rest_framework import viewsets
from accounts.models.professor import Professor
from accounts.serializers import ProfessorSerializer
from accounts.permissions import IsItManager


class ProfessorViewSetITAdmin(viewsets.ModelViewSet):
    model = Professor
    permission_classes = [IsItManager]
    serializer_class = ProfessorSerializer



