from rest_framework import serializers
from accounts.models import professor


class ProfessorSerializerITAdmin(serializers.ModelSerializer):
    class Meta:
        model = professor
        fields = '__all__'
