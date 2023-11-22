from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from accounts.permissions import IsITAdmin
from college.serializers.faculty import FacultySerializer
from college.models import Faculty


@extend_schema(tags=["faculty"])
class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated, IsITAdmin]
    http_method_names = ['get', 'post', 'put', 'delete']
