# Generated by Django 5.1.3 on 2024-12-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0011_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='OktCnZJrFU9ARPVmJcM0TEVrNyoTFNWY', max_length=32),
        ),
    ]
