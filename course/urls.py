from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'course'
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename="course")
router.register(r'term-courses', views.TermCourseViewSet, basename="term-course")

urlpatterns = [
    path('', include(router.urls)),
]
