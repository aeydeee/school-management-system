# Generated by Django 5.1.3 on 2024-12-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0007_remove_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='ScPCYWeeavpoxuebbQj5DF8se4hzgP3T', max_length=32),
        ),
    ]