from django.urls import include, path
from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

app_name = 'accounts'


urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
