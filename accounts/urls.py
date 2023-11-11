from django.urls import include, path
from django.urls import path
from .views import *

app_name = 'accounts'
# router = routers.DefaultRouter()


urlpatterns = [
    # path('login/', LoginAPIView.as_view(), name="login"),
    # path('logout/', VerifyEmail.as_view(), name="logout"),
    path('change-password-request/', ChangePasswordRequestView.as_view(), name='change_password_request'),
    path('change-password-action/<uidb64>/<token>/', ChangePasswordActionView.as_view(), name='change_password_action'),
]
