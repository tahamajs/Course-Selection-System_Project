from rest_framework import serializers


class ChangePasswordActionSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
