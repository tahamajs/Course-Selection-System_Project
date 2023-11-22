from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Professor

User = get_user_model()


class ProfessorSerializer(serializers.ModelSerializer):
    user_user_no = serializers.ReadOnlyField(source='user.user_no')
    user_first_name = serializers.CharField(source='user.first_name')
    user_last_name = serializers.CharField(source='user.last_name')
    user_email = serializers.CharField(source='user.email')
    user_phone_number = serializers.CharField(source='user.phone_number')

    class Meta:
        model = Professor
        fields = ['user_user_no', 'user_first_name', 'user_last_name', 'user_email', 'user_phone_number']

    def update(self, instance, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user', {})
        user = instance.user

        for key, value in user_data.items():
            setattr(user, key, value)

        user.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class ProfessorSerializerAllFields(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        depth = 1
