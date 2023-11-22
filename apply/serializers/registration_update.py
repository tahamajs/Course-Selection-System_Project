from rest_framework import serializers
from apply.models import RegistrationUpdate
from accounts.models import Student


class RegistrationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationUpdate
        fields = ['add_courses', 'del_courses', 'approval_status', ]
        read_only_fields = ['approval_status', ]

    def create(self, validated_data):
        student = Student.objects.get(user=self.context['request'].user)
        obj = RegistrationUpdate.objects.create(student=student, )
        obj.add_courses.set(validated_data['add_courses'])
        obj.del_courses.set(validated_data['del_courses'])
        return obj
