from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Teacher, Group, Faculty
from .forms import StudentForm, StudentDeleteForm, TeacherForm, TeacherDeleteForm, GroupForm, GroupDeleteForm, FacultyForm, FacultyDeleteForm

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

def teacher(request, teacher_id):
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
        form = TeacherDeleteForm(instance=teacher)

    return render(request, 'students/delete_teacher.html',
                  {
                      'form': form,
                      'teacher': teacher,
                  })
                   
def groups(request): 
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'students/groups.html', context)                  

def group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = Student.objects.filter(group__id=group.pk)
    try:    
        teacher = Teacher.objects.get(group__id=group.pk)
    except Teacher.DoesNotExist:
        teacher = None
    return render(request, 'students/group.html', {'group': group, 'students': students, 'teacher': teacher})

def insert_group(request): 
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm()
    return render(request, 'students/insert_group.html', {'form' : form})

def edit_group(request, group_id=None):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group', group_id=group_id)
    else:
        form = GroupForm(instance=group)
    return render(request, 'students/edit_group.html', {'form' : form, 'group': group})

def delete_group(request, group_id=None):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == "POST":
        form = GroupDeleteForm(request.POST,
                              instance=group)
        if form.is_valid():
            group.delete()
            return redirect('groups')
    else:
        form = GroupDeleteForm(instance=group)

    return render(request, 'students/delete_group.html',
                  {
                      'form': form,
                      'group': group,
                  })

def faculties(request): 
    faculties = Faculty.objects.all()
    context = {'faculties': faculties}
    return render(request, 'students/faculties.html', context)                  

def faculty(request, faculty_id):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    groups = Group.objects.filter(faculty__id=faculty_id)
    return render(request, 'students/faculty.html', {'groups': groups, 'faculty': faculty})

def insert_faculty(request): 
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculties')
    else:
        form = FacultyForm()
    return render(request, 'students/insert_faculty.html', {'form' : form})

def edit_faculty(request, faculty_id=None):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty', faculty_id=faculty_id)
    else:
        form = FacultyForm(instance=faculty)
    return render(request, 'students/edit_faculty.html', {'form' : form, 'faculty': faculty})

def delete_faculty(request, faculty_id=None):
    faculty = get_object_or_404(Faculty, pk=faculty_id)
    if request.method == "POST":
        form = FacultyDeleteForm(request.POST,
                              instance=faculty)
        if form.is_valid():
            faculty.delete()
            return redirect('faculties')
    else:
        form = FacultyDeleteForm(instance=faculty)

    return render(request, 'students/delete_faculty.html',
                  {
                      'form': form,
                      'faculty': faculty,
                  })
    
