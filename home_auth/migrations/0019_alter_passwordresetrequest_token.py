# Generated by Django 5.1.3 on 2024-12-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0018_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='DwSWoqIeAC62UrhQhDqdW6FXtmIUX3eQ', max_length=32),
        ),
    ]
