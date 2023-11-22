from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from accounts.models.professor import Professor
from accounts.serializers.serializer_professor import ProfessorSerializerITAdmin
from accounts.permissions import IsITAdmin


@extend_schema(tags=["professor"])
class ProfessorViewSetITAdmin(viewsets.ModelViewSet):
    model = Professor
    permission_classes = [IsITAdmin]
    serializer_class = ProfessorSerializerITAdmin
    http_method_names = ['get', 'post', 'put', 'delete']
