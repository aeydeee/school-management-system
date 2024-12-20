from django.db import models
from django.utils.text import slugify

from home_auth.models import CustomUser


# Create your models here.
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=100)

    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    mother_email = models.EmailField(max_length=100)

    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self) -> str:
        return f"{self.father_name} & {self.mother_name}"


class Student(models.Model):
    student_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=15)
    student_image = models.ImageField(upload_to='students/', default='students/profile.png')
    slug = models.CharField(max_length=255, unique=True, blank=True)

    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    section = models.ForeignKey('class_group.Section', on_delete=models.SET_NULL, null=True, related_name='students')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.user:  # Make sure user exists before trying to access attributes
            if not self.slug:
                self.slug = slugify(f'{self.user.first_name}-{self.user.last_name}-{self.student_id}')
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.student_id})'
