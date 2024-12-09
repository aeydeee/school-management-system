from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from department.models import Department
from teacher.models import Teacher


# Create your models here.
class Subject(models.Model):
    code = models.CharField(max_length=45)
    name = models.CharField(max_length=100)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')

    class Meta:
        constraints = [
            UniqueConstraint(Lower('code'), name='unique_lower_code'),
            UniqueConstraint(Lower('name'), name='unique_lower_name'),
        ]

    def clean(self):
        # Check for case-insensitive uniqueness in Python
        if Subject.objects.filter(name__iexact=self.name).exists():
            raise ValidationError({'name': 'A subject with this name already exists.'})
        if Subject.objects.filter(code__iexact=self.code).exists():
            raise ValidationError({'code': 'A subject with this code already exists.'})


class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')


class Section(models.Model):
    name = models.CharField(max_length=15)
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='sections')
