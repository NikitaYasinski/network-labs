from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    number = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, related_name='faculty', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name        




