from rest_framework import serializers
from accounts.models import Professor


class ProfessorSerializerITAdmin(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
