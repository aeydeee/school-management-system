from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class UsernameOrEmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if it's an email
            if '@' in username:
                user = CustomUser.objects.get(email=username)
            else:
                user = CustomUser.objects.get(username=username)

            # Verify password
            if user and user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
