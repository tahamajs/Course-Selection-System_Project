from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from accounts.filters.educational_deputy import EducationalDeputyFilter
from accounts.models.educational_deputy import EducationalDeputy
from accounts.serializers.educational_deputy import EducationalDeputySerializer


@extend_schema(tags=["educational_deputy"])
class EducationalDeputyViewSet(ModelViewSet):
    queryset = EducationalDeputy.objects.all()
    serializer_class = EducationalDeputySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = EducationalDeputyFilter
    http_method_names = ['get', 'post', 'put', 'delete']
