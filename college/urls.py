from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views.faculty import FacultyViewSet
from .views.term import TermViewSet

app_name = 'college'
router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'terms', TermViewSet, basename='term')

urlpatterns = router.urls
