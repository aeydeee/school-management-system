# Generated by Django 5.1.3 on 2024-12-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0017_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='bOsuNwZheaMZ0nmDpbBV4tCby8LlbPQY', max_length=32),
        ),
    ]