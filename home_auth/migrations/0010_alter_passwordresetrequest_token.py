# Generated by Django 5.1.3 on 2024-12-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0009_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='42aoE8JTfEJa8BygYTBUS3R3LoqTMhk4', max_length=32),
        ),
    ]
