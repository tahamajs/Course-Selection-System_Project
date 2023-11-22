from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from accounts.models import *
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
import shared.utils as utils
from django.contrib.auth import get_user_model
from accounts.serializers import ChangePasswordRequestSerializer


User = get_user_model()


@extend_schema(tags=["Change password request"])
class ChangePasswordRequestView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordRequestSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        if self.queryset.filter(email=email).exists():
            user = self.queryset.get(email=email)
            user_id_b64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request=request).domain

            reset_url = 'http://' + current_site + reverse_lazy('accounts:change_password_action',
                                                                kwargs={'uidb64': user_id_b64, 'token': token})
            utils.send_password_reset_email(reset_url, email)
        return Response({'successfully': 'check your email to reset your password'}, status=status.HTTP_200_OK)


