from rest_framework import permissions

from accounts.models import Student


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Student.objects.filter(user=request.user).exists()
