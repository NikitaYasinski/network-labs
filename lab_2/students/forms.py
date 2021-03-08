from django.forms import ModelForm
from .models import Student, Teacher, Group, Faculty

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentDeleteForm(ModelForm):
    class Meta:
        model = Student
        fields = []

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherDeleteForm(ModelForm):
    class Meta:
        model = Teacher
        fields = []

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class GroupDeleteForm(ModelForm):
    class Meta:
        model = Group
        fields = []

class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class FacultyDeleteForm(ModelForm):
    class Meta:
        model = Faculty
        fields = []