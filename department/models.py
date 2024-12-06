from django.db import models

from teacher.models import Teacher


# Create your models here.
class Department(models.Model):
    department_id = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    head_of_department = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True,
                                              related_name='departments')
    start_date = models.DateField()
