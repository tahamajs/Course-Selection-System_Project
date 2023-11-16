from rest_framework import permissions

from accounts.models import EducationalDeputy


class IsEducationalDeputy(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and EducationalDeputy.objects.filter(user=request.user).exists()
