from rest_framework import permissions
from accounts.models import EducationalDeputy
from . import helper


class IsFacultyEducationalDeputy(permissions.BasePermission):
    def has_permission(self, request, view):
        return helper.has_faculty_permission(EducationalDeputy, request, view)
