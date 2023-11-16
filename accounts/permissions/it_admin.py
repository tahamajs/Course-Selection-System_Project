from rest_framework import permissions

from accounts.models import ITAdmin


class IsITAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and ITAdmin.objects.filter(user=request.user).exists()
