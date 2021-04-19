from django.shortcuts import render, redirect
import requests
import json

def students(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/students')
        data = response.json()
        return render(request, 'university/students.html', {
            'students': data,
        })
    if request.method == 'POST':
        student = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'group': request.POST.get('group')
        }
        print(json.dumps(student))
        headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
        requests.post('http://localhost:8000/students/', json=json.dumps(student), headers=headers)
        return redirect('students')  

def student(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/students/{id}')
        data = response.json()
        return render(request, 'university/student.html', {
            'student': data,
        })

def teachers(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/teachers')
        data = response.json()
        return render(request, 'university/teachers.html', {
            'teachers': data,
        })
    if request.method == 'POST':
        teacher = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'subject': request.POST.get('subject'),
            'group': request.POST.get('group')
        }
        print(json.dumps(teacher))
        headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
        requests.post('http://localhost:8000/teachers/', json=json.dumps(teacher), headers=headers)
        return redirect('teachers')

def teacher(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/teachers/{id}')
        data = response.json()
        return render(request, 'university/teacher.html', {
            'teacher': data,
        })

def groups(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/groups')
        data = response.json()
        return render(request, 'university/groups.html', {
            'groups': data,
        })

def group(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/groups/{id}')
        data = response.json()
        return render(request, 'university/group.html', {
            'group': data,
        })

def faculties(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/faculties')
        data = response.json()
        return render(request, 'university/faculties.html', {
            'faculties': data,
        })

def faculty(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/faculties/{id}')
        data = response.json()
        return render(request, 'university/faculty.html', {
            'faculty': data,
        })