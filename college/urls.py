#urls.py file
from django.urls import path
from college.views import TermDetailAPIView , TermListAPIView ,StudentCoursesAPIView, TermViewSet

urlpatterns = [
    path('terms/', TermListAPIView.as_view()),
    path('term/<int:pk>/', TermDetailAPIView.as_view()),
    path('student/<str:pk>/my-courses/', StudentCoursesAPIView.as_view(), name='student-courses'),
    path('admin/term/', TermViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admin/term/<int:pk>/', TermViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    ]