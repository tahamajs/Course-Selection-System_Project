from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'college'
router = DefaultRouter()
router.register(r'faculty', views.FacultyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
