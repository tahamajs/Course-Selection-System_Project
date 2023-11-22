from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission
from accounts.models.educational_deputy import EducationalDeputy
from accounts.models.student import Student
from accounts.models.professor import Professor


class EducationalDeputyOrStudentOrProfessorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == 'GET' and EducationalDeputy.objects.filter(user=request.user).exists():
                return True
            elif request.method == 'PUT' and (
                    Student.objects.filter(user=request.user).exists() or Professor.objects.filter(
                user=request.user).exists()):
                return True
        return False
