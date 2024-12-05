# context_processors.py
from django.http import JsonResponse, HttpResponseForbidden

from school.models import Notification


def add_active_page(request):
    print(f"Current URL Name: {request.resolver_match.url_name}")
    return {'active_page': request.resolver_match.url_name}


def current_user_group(request):
    # Check if the user is authenticated and return their groups
    if request.user.is_authenticated:
        return {
            'user_groups': request.user.groups.all()  # This gives you a queryset of groups
        }
    return {
        'user_groups': []  # Return an empty list if the user is not authenticated
    }


def notification(request):
    unred_notif = 0
    unread_notification = None

    notifications = Notification.objects.filter(user=request.user.id)
    if request.user:
        try:
            unread_notification = Notification.objects.filter(user=request.user.id, is_read=False)
            unred_notif = unread_notification.count()
        except Notification.DoesNotExist:
            unred_notif = 0
        except Exception as e:
            print(f"Error processing notification: {e}")
            unred_notif = 0

    elif request.user.groups.filter(name='admin').exists():
        try:
            all_notifications = Notification.objects.all()
            unred_notif = all_notifications.count()
        except Notification.DoesNotExist:
            unred_notif = 0
        except Exception as e:
            print(f"Error processing notification: {e}")
            unred_notif = 0
    else:
        unred_notif = 0

    # This part should not be reachable after the above return statements.
    return {
        'unread_notification_count': unred_notif,
        'notifications': notifications,
    }
