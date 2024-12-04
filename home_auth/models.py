from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import models, migrations
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    is_authorized = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,  # Use Django's Group model to manage roles
        related_name='custom_users',  # You can reverse query users belonging to the group
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,  # Permissions directly related to users
        related_name='custom_users',  # Reverse lookup for permissions
        blank=True
    )

    def __str__(self):
        return self.username


class PasswordResetRequest(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(max_length=32, default=get_random_string(32), editable=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Define token validity period (e.g., 1 hour)
    TOKEN_VALIDITY_PERIOD = timezone.timedelta(hours=1)

    def is_valid(self):
        return timezone.now() <= self.created_at + self.TOKEN_VALIDITY_PERIOD

    def send_reset_email(self, request):
        reset_link = reverse('reset_password', kwargs={'token': self.token})
        domain = get_current_site(request).domain
        full_link = f"http://{domain}{reset_link}"
        send_mail(
            'Password Reset Request',
            f'Click the following link to reset your password: {full_link}',
            settings.DEFAULT_FROM_EMAIL,
            [self.email],
            fail_silently=False,
        )
