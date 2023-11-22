from django_filters.rest_framework import FilterSet
from accounts.models.educational_deputy import EducationalDeputy


class EducationalDeputyFilter(FilterSet):
    class Meta:
        model = EducationalDeputy
        fields = {
            'user__first_name': ['exact', 'icontains'],
            'user__last_name': ['exact', 'icontains'],
            'user__user_no': ['exact', 'icontains'],
            'user__national_code': ['exact', 'icontains'],
            'faculty__name': ['exact', 'icontains'],
            'field_of_study__name': ['exact', 'icontains'],
        }
