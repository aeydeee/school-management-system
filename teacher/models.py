from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=15)
    section = models.CharField(max_length=15)
    student_image = models.ImageField(upload_to='students/', default='students/profile.png')
    slug = models.CharField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name}-{self.last_name}-{self.student_id}')
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.student_id})'
