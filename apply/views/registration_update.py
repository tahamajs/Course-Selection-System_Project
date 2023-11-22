from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apply.models import RegistrationUpdate
from apply.serializers import RegistrationUpdateSerializer

from accounts.permissions import IsITAdmin


@extend_schema(tags=["registration update"])
class RegistrationUpdateViewSet(viewsets.ModelViewSet):
    queryset = RegistrationUpdate.objects.all()
    serializer_class = RegistrationUpdateSerializer
    permission_classes = [IsAuthenticated, IsITAdmin, ]
    http_method_names = ['get', 'post']
