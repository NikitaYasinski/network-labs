from rest_framework import serializers
from .models import Student, Group, Teacher, Faculty

class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    faculty = serializers.SlugRelatedField(
        slug_field='name',
        queryset = Faculty.objects.all()
     )
    
    class Meta:
        model = Group
        fields = ('id', 'number', 'faculty')

    

class StudentSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='number',
        queryset = Group.objects.all()
     )

    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'phone', 'group')


class TeacherSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='number',
        queryset = Group.objects.all()
    )

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'email', 'phone', 'subject', 'group')

