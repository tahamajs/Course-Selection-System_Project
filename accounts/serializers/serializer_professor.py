from rest_framework import serializers
from accounts.models import Professor, User
from college.models import Faculty
from college.models import FieldOfStudy
from shared.models import Expertise
from shared.models import Degree
from course.models import Course


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


class UserFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'national_code', 'gender', 'birth_date']


class FacultyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name']


class FieldOfStudyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = ['name', 'units', 'group', 'degree']


class ExpertiseFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ['name']


class DegreeFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['name']


class CourseFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'credits', 'course_type', 'faculty']


class ProfessorSerializerAllFields(serializers.ModelSerializer):
    faculty = FacultyFieldsSerializer()
    user = UserFieldsSerializer()
    field_of_study = FieldOfStudyFieldsSerializer()
    expertise = ExpertiseFieldsSerializer()
    degree = DegreeFieldsSerializer()
    past_teaching_courses = CourseFieldsSerializer(many=True)

    class Meta:
        model = Professor
        fields = ['user', 'faculty', 'field_of_study', 'expertise', 'degree', 'past_teaching_courses']


class ProfessorSerializerITAdmin(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
