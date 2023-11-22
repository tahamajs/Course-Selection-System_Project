from rest_framework import serializers
from college.models import Faculty


class ChangePasswordActionSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


