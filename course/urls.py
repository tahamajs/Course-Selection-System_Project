from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'course'
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'term-courses', views.TermCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
