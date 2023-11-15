from rest_framework import serializers
from college.models import Faculty


class ChangePasswordActionSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
