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
        headers = {'Content-Type': 'application/json'}
        requests.post('http://localhost:8000/students/', data=json.dumps(student), headers=headers)
        return redirect('students')  

def student(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/students/{id}')
        data = response.json()
        return render(request, 'university/student.html', {
            'student': data,
        })
    if request.method == 'POST':
        method = request.POST.get('_method', '').lower()
        if method == 'delete':
            requests.delete(f'http://localhost:8000/students/{id}')
            return redirect('students')
        if method == 'put':
            student = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
                'group': request.POST.get('group')
            }   
            headers = {'Content-Type': 'application/json'}
            requests.put(f'http://localhost:8000/students/{id}/', data=json.dumps(student), headers=headers)
            return redirect('student', id)

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
        headers = {'Content-Type': 'application/json'}
        requests.post('http://localhost:8000/teachers/', data=json.dumps(teacher), headers=headers)
        return redirect('teachers')

def teacher(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/teachers/{id}')
        data = response.json()
        return render(request, 'university/teacher.html', {
            'teacher': data,
        })
    if request.method == 'POST':
        method = request.POST.get('_method', '').lower()
        if method == 'delete':
            requests.delete(f'http://localhost:8000/teachers/{id}')
            return redirect('teachers')
        if method == 'put':
            teacher = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
                'subject': request.POST.get('subject'),
                'group': request.POST.get('group')
            }   
            headers = {'Content-Type': 'application/json'}
            requests.put(f'http://localhost:8000/teachers/{id}/', data=json.dumps(teacher), headers=headers)
            return redirect('teacher', id)

def groups(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/groups')
        data = response.json()
        return render(request, 'university/groups.html', {
            'groups': data,
        })
    if request.method == 'POST':
        group = {
            'number': request.POST.get('number'),
            'faculty': request.POST.get('faculty')
        }
        headers = {'Content-Type': 'application/json'}
        requests.post('http://localhost:8000/groups/', data=json.dumps(group), headers=headers)
        return redirect('groups')

def group(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/groups/{id}')
        data = response.json()
        return render(request, 'university/group.html', {
            'group': data,
        })
    if request.method == 'POST':
        method = request.POST.get('_method', '').lower()
        if method == 'delete':
            requests.delete(f'http://localhost:8000/groups/{id}')
            return redirect('groups')
        if method == 'put':
            group = {
                'number': request.POST.get('number'),
                'faculty': request.POST.get('faculty')
            }   
            headers = {'Content-Type': 'application/json'}
            requests.put(f'http://localhost:8000/groups/{id}/', data=json.dumps(group), headers=headers)
            return redirect('group', id)
   
def faculties(request):
    if request.method == 'GET':
        response = requests.get('http://localhost:8000/faculties')
        data = response.json()
        return render(request, 'university/faculties.html', {
            'faculties': data,
        })
    if request.method == 'POST':
        faculty = {
            'name': request.POST.get('name')
        }
        headers = {'Content-Type': 'application/json'}
        requests.post('http://localhost:8000/faculties/', data=json.dumps(faculty), headers=headers)
        return redirect('faculties')

def faculty(request, id):
    if request.method == 'GET':
        response = requests.get(f'http://localhost:8000/faculties/{id}')
        data = response.json()
        return render(request, 'university/faculty.html', {
            'faculty': data,
        })
    if request.method == 'POST':
        method = request.POST.get('_method', '').lower()
        if method == 'delete':
            requests.delete(f'http://localhost:8000/faculties/{id}')
            return redirect('faculties')
        if method == 'put':
            faculty = {
                'name': request.POST.get('name')
            }   
            headers = {'Content-Type': 'application/json'}
            requests.put(f'http://localhost:8000/faculties/{id}/', data=json.dumps(faculty), headers=headers)
            return redirect('faculty', id)