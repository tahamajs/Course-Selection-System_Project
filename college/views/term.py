from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from college.models.term import Term
from college.serializers.term import TermSerializer
from accounts.permissions import IsITAdmin


@extend_schema(tags=["term"])
class TermViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated, IsITAdmin]
