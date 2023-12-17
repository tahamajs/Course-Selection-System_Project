from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt import views as jwt_views
from .views.educational_deputy import EducationalDeputyViewSet
from .views.professor import ProfessorViewSetITAdmin, ProfessorViewSet
from .views.student import StudentViewSetITAdmin, StudentViewSet

app_name = 'accounts'
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'professors', ProfessorViewSet, basename='professor')
router.register(r'admin/students-itadmin', StudentViewSetITAdmin, basename='student-itadmin')
router.register(r'admin/professors-itadmin', ProfessorViewSetITAdmin, basename='professor-itadmin')
router.register(r'admin/educationaldeputies', EducationalDeputyViewSet, basename='educationaldeputy')

urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password-request/', ChangePasswordRequestView.as_view(), name='change_password_request'),
    path('change-password-action/<uidb64>/<token>/', ChangePasswordActionView.as_view(), name='change_password_action')
] + router.urls


