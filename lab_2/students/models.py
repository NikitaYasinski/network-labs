from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    math_score = models.IntegerField()
    physics_score = models.IntegerField()
    chemistry_score = models.IntegerField()
    biology_score = models.IntegerField()

    def __str__(self):
        return (self.math_score, self.physics_score, self.chemistry_score, self.biology_score)