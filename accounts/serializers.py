from rest_framework import serializers

class ChangePasswordActionSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    one_time_code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
