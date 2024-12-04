from django.db import migrations
from django.contrib.auth.models import Group


def create_groups(apps, schema_editor):
    # Define the groups to create
    groups = ['student', 'teacher', 'admin']
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)


class Migration(migrations.Migration):
    dependencies = [
        # Add the previous migration file name (e.g., 0002_auto_...), ensuring dependencies are correct
        ('home_auth', '0004_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
