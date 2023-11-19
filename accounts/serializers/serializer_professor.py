from rest_framework import serializers
from accounts.models import professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = professor
        fields = '__all__'
