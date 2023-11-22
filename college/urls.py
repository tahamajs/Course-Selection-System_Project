from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from college.views import TermDetailAPIView , TermListAPIView ,StudentCoursesAPIView, TermViewSet


app_name = 'college'
router = DefaultRouter()
router.register(r'faculty', views.FacultyViewSet)


urlpatterns = [
    path('terms/', TermListAPIView.as_view()),
    path('term/<int:pk>/', TermDetailAPIView.as_view()),
    path('student/<str:pk>/my-courses/', StudentCoursesAPIView.as_view(), name='student-courses'),
    path('admin/term/', TermViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admin/term/<int:pk>/', TermViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', include(router.urls))
]
