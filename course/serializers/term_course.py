from rest_framework import serializers
from course.models import TermCourse


class TermCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCourse
        fields = '__all__'
