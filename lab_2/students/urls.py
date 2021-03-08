from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>', views.student, name='student'),
    path('insert_student', views.insert_student, name='insert_student'),
    path('edit_student/<int:student_id>', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>', views.delete_student, name='delete_student'),
]