# Generated by Django 5.1.3 on 2024-12-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class_group', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(related_name='classes', to='student.student'),
        ),
    ]