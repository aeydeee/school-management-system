from django.db import models
from django.utils.text import slugify

from home_auth.models import CustomUser


class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.city} {self.zip_code} {self.country}'


# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    qualification = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    teacher_image = models.ImageField(upload_to='teachers/', default='teachers/profile.png')
    slug = models.CharField(max_length=255, unique=True, blank=True)

    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.user:  # Make sure user exists before trying to access attributes
            if not self.slug:
                self.slug = slugify(f'{self.user.first_name}-{self.user.last_name}-{self.teacher_id}')
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.teacher_id})'
