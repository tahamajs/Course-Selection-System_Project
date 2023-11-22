from rest_framework import permissions

from accounts.models import Professor


class IsProfessor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Professor.objects.filter(user=request.user).exists()
