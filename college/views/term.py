from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from college.models.term import Term
from college.serializers.term import TermSerializer
from accounts.permissions import IsITAdmin


class TermViewSet(viewsets.ModelViewSet):
    http_method_names = ['GET']
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated, IsITAdmin]
