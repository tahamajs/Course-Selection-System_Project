from django.urls import path
from rest_framework import routers
from accounts.views.educational_deputy import EducationalDeputyViewSet
from .views import *
from rest_framework_simplejwt import views as jwt_views
from .views.faculty import FacultyViewSet

app_name = 'users'
router = routers.DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'admin/educationaldeputies', EducationalDeputyViewSet, basename='educationaldeputy')


urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password-request/', ChangePasswordRequestView.as_view(), name='change_password_request'),
    path('change-password-action/<uidb64>/<token>/', ChangePasswordActionView.as_view(), name='change_password_action')
] + router.urls


