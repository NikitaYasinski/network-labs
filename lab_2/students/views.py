from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher
from .forms import StudentForm, StudentDeleteForm, TeacherForm, TeacherDeleteForm

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

def teachers(request): 
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'students/teachers.html', context)                  

def teacher(request, student_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request, 'students/teacher.html', {'teacher': teacher})

def insert_teacher(request): 
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'students/insert_teacher.html', {'form' : form})

def edit_teacher(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher', teacher_id=teacher_id)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'students/edit_teacher.html', {'form' : form, 'teacher': teacher})

def delete_teacher(request, teacher_id=None):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == "POST":
        form = TeacherDeleteForm(request.POST,
                              instance=teacher)
        if form.is_valid():
            teacher.delete()
            return redirect('teachers')
    else:
        form = TeacherDeleteForm(instance=Teacher)

    return render(request, 'students/delete_teacher.html',
                  {
                      'form': form,
                      'teacher': teacher,
                  })
                   
    
