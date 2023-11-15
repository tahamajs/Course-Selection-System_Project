from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from accounts.serializers import FacultySerializer
from college.models import Faculty


class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]
