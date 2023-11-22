from rest_framework import serializers
from accounts.models.educational_deputy import EducationalDeputy

class EducatinalDeputySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDeputy
        fields = '__all__'