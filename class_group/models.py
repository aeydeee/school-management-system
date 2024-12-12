from django.db import models

from teacher.models import Teacher
from subject.models import Subject


# Create your models here.
class Section(models.Model):
    grade_level = models.IntegerField()
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name} (Grade {self.grade_level})"


class Class(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes', null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='classes', null=True)

    students = models.ManyToManyField('student.Student', related_name='classes')

    def __str__(self):
        subject_name = self.subject.name if self.subject else "No Subject"
        return f"{self.name} ({subject_name})"
