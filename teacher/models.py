from django.db import models
from django.utils.text import slugify


class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=100)


# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    qualification = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    teacher_image = models.ImageField(upload_to='teachers/', default='teachers/profile.png')
    slug = models.CharField(max_length=255, unique=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name}-{self.last_name}-{self.teacher_id}')
        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.teacher_id})'
