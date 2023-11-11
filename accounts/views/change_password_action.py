from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from accounts.models import User 
from accounts.serializers import ChangePasswordActionSerializer 
from rest_framework import exceptions


class ChangePasswordActionView(generics.GenericAPIView):
    serializer_class = ChangePasswordActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        one_time_code = serializer.validated_data['one_time_code']
        new_password = serializer.validated_data['new_password']

        try:
            user = User.objects.get(email=email)
            user_id = urlsafe_base64_decode(kwargs['uidb64']).decode('utf-8')
            
            if user.id != int(user_id):
                raise exceptions.AuthenticationFailed('Invalid user')

            if not PasswordResetTokenGenerator().check_token(user, one_time_code):
                raise exceptions.AuthenticationFailed('Invalid or expired one-time code')

            user.set_password(new_password)
            user.save()

            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

        except (User.DoesNotExist, DjangoUnicodeDecodeError):
            raise exceptions.AuthenticationFailed('Invalid user or one-time code')
