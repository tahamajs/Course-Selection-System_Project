from django.urls import include, path
from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

app_name = 'accounts'
# router = routers.DefaultRouter()


urlpatterns = [
    # path('login/', LoginAPIView.as_view(), name="login"),
    # path('logout/', VerifyEmail.as_view(), name="logout"),
    path('change-password-request/', ChangePasswordRequestView.as_view(), name='change_password_request'),
    path('change-password-action/<uidb64>/<token>/', ChangePasswordActionView.as_view(), name='change_password_action'),

]
app_name = 'accounts'


urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
