from rest_framework import serializers


class ChangePasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
