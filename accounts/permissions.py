# permissions.py

from rest_framework import permissions
from .models import ITAdmin , Student , Professor


class IsItManager(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.is_authenticated and ITAdmin.objects.get(user=request.user).exists():
            return True
        return False


class IsProfessorOrStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if Student.objects.filter(user=request.user) or Professor.objects.filter(user=request.user):
                return True
        return False
