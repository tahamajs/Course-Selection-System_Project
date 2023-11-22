from django_filters.rest_framework import FilterSet
from accounts.models.professor import Professor


class ProfessorFilter(FilterSet):
    class Meta:
        model = Professor
        fields = {
            'user__firstname': ['exact', 'icontains'],
            'user__lastname': ['exact', 'icontains'],
            'user__user_no': ['exact', 'icontains'],
            'faculty__name': ['exact', 'icontains'],
            'field_of_study__name': ['exact', 'icontains'],
            'expertise__name': ['exact', 'icontains'],
            'degree__name': ['exact', 'icontains'],
            'past_teaching_courses__name': ['exact', 'icontains'],
        }
