from rest_framework import permissions
from accounts.models import EducationalDeputy


class IsEducationalDeputyOfCourseFaculty(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user_obj = EducationalDeputy.objects.get(user=request.user)
            is_same_faculty = view.queryset.filter(
                id=view.kwargs['pk']).filter(faculty=user_obj.faculty).exists()
            return user_obj and is_same_faculty
        except:
            return False
