from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>', views.student, name='student'),
    path('insert_student', views.insert_student, name='insert_student'),
    path('edit_student/<int:student_id>', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>', views.delete_student, name='delete_student'),
    path('teachers', views.teachers, name='teachers'),
    path('teachers/<int:teacher_id>', views.teacher, name='teacher'),
    path('insert_teacher', views.insert_teacher, name='insert_teacher'),
    path('edit_teacher/<int:teacher_id>', views.edit_teacher, name='edit_teacher'),
    path('delete_student/<int:teacher_id>', views.delete_teacher, name='delete_teacher'),
]