from django.urls import path

from . import views

urlpatterns = [
    path('students', views.students, name='students'),
    path('students/<int:id>/', views.student, name='student'),
    path('groups', views.groups, name='groups'),
    path('groups/<int:id>/', views.group, name='group'),
    path('teachers', views.teachers, name='teachers'),
    path('teachers/<int:id>/', views.teacher, name='teacher'),
    path('faculties', views.faculties, name='faculties'),
    path('faculties/<int:id>/', views.faculty, name='faculty'),
]