from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Student, User, Professor
from college.models import Faculty, FieldOfStudy
from course.models.course import Course


class StudentSerializer(serializers.ModelSerializer):
    user_user_no = serializers.ReadOnlyField(source='user.user_no')
    user_first_name = serializers.CharField(source='user.first_name')
    user_last_name = serializers.CharField(source='user.last_name')
    user_email = serializers.CharField(source='user.email')
    user_phone_number = serializers.CharField(source='user.phone_number')

    class Meta:
        model = Student
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


class SupervisorUserFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class FacultyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['name']


class FieldOfStudyFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = ['name', 'units', 'group', 'degree']


class SupervisorFieldsSerializer(serializers.ModelSerializer):
    user = SupervisorUserFieldsSerializer()

    class Meta:
        model = Professor
        fields = ['user']


class CoursesPassedFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'credits', 'course_type', 'faculty']


class CoursesTakenFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'credits', 'course_type', 'faculty']


class StudentSerializerAllFields(serializers.ModelSerializer):
    user = UserFieldsSerializer()
    faculty = FacultyFieldsSerializer()
    field_of_study = FieldOfStudyFieldsSerializer()
    supervisor = SupervisorFieldsSerializer()
    courses_passed = CoursesPassedFieldsSerializer(many=True)
    courses_taken = CoursesTakenFieldsSerializer(many=True)

    class Meta:
        model = Student
        fields = ['entry_term', 'entry_year', 'gpa', 'military_service_status', 'academic_years', 'user', 'faculty',
                  'field_of_study', 'supervisor', 'courses_passed', 'courses_taken']


class StudentSerializerITAdmin(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
