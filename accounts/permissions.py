from rest_framework import permissions

from accounts.models.it_admin import ITAdmin


class IsItManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and ITAdmin.objects.filter(user=request.user):
            return True
        else:
            return False
