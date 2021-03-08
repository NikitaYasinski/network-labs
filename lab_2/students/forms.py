from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']

class StudentDeleteForm(ModelForm):
    class Meta:
        model = Student
        fields = []