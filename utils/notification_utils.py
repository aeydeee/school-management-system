from home_auth.models import CustomUser
from school.models import Notification


def create_notification(user, message):
    try:
        user = CustomUser.objects.get(username=user.username)  # Replace 'user_id' with actual ID
    except CustomUser.DoesNotExist:
        raise ValueError("User does not exist.")

    create_notif = Notification.objects.create(user=user, message=message)

    return create_notif
