from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    message = serializers.CharField(default="Logout successful")
