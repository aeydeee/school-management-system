# Generated by Django 5.1.3 on 2024-12-11 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_group', '0004_alter_class_section'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='subject.subject'),
        ),
    ]
