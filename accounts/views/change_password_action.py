from drf_spectacular.openapi import AutoSchema
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from accounts.models import User
from accounts.serializers.change_password_action import ChangePasswordActionSerializer
from rest_framework import exceptions
from drf_spectacular.views import extend_schema


class ChangePasswordActionView(generics.GenericAPIView):
    serializer_class = ChangePasswordActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.validated_data['new_password']

        try:
            token = kwargs['token']
            user_id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise exceptions.AuthenticationFailed('Invalid or expired one-time code')

            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

        except (User.DoesNotExist, DjangoUnicodeDecodeError):
            raise exceptions.AuthenticationFailed('Invalid user or one-time code')
