from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apply.models import RegistrationUpdate
from apply.serializers import RegistrationUpdateSerializer

from accounts.permissions import IsITAdmin


class RegistrationUpdateViewSet(viewsets.ModelViewSet):
    queryset = RegistrationUpdate.objects.all()
    serializer_class = RegistrationUpdateSerializer
    permission_classes = [IsAuthenticated, IsITAdmin, ]
