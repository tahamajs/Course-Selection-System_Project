from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from accounts.serializers import LogoutSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    # @extend_schema(responses=LogoutSerializer)
    def post(self, request):
        serializer = self.serializer_class(data={'message': 'Logout successful'})
        serializer.is_valid()

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
