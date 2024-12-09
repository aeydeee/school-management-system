# Generated by Django 5.1.3 on 2024-12-09 07:48

import django.db.models.deletion
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=45)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='department.department')),
            ],
            options={
                'constraints': [models.UniqueConstraint(django.db.models.functions.text.Lower('code'), name='unique_lower_code'), models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='unique_lower_name')],
            },
        ),
    ]
