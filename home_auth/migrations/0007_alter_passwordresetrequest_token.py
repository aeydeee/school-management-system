# Generated by Django 5.1.3 on 2024-12-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0006_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='M6vQ8PzotulbYJzQ2QBSg4EkhSJDG71N', max_length=32),
        ),
    ]
