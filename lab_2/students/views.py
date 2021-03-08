from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm, StudentDeleteForm

def index(request): 
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/index.html', context)

def student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/student.html', {'student': student})

def insert_student(request): 
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'students/insert_student.html', {'form' : form})

def edit_student(request, student_id=None):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student', student_id=student_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form' : form, 'student': student})

def delete_student(request, student_id=None):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentDeleteForm(request.POST,
                              instance=student)
        if form.is_valid():
            student.delete()
            return redirect('index')
    else:
        form = StudentDeleteForm(instance=student)

    return render(request, 'students/delete_student.html',
                  {
                      'form': form,
                      'student': student,
                  })
    
