# Generated by Django 5.1.3 on 2024-12-05 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='head_of_dep',
            new_name='head_of_department',
        ),
    ]