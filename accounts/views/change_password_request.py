from rest_framework import exceptions, generics, serializers
from rest_framework.response import Response
from rest_framework import status
from accounts.models import *
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
import shared.utils as utils


class ChangePasswordRequestView(generics.GenericAPIView):
    queryset = User.objects.all()

    def post(self, request):
        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user_id_b64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request=request).domain

            reset_url = 'http://' + current_site + reverse_lazy('accounts:change_password_action',
                                                                kwargs={'uidb64': user_id_b64, 'token': token})
            utils.send_password_reset_email(reset_url, email)
        return Response({'successfully': 'check your email to reset your password'}, status=status.HTTP_200_OK)
