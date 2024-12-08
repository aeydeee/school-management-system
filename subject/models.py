from django.db import models

from department.models import Department
from teacher.models import Teacher


# Create your models here.
class Subject(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=100)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')


class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')


class Section(models.Model):
    name = models.CharField(max_length=15)
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='sections')
