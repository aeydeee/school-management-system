# context_processors.py
from django.http import JsonResponse, HttpResponseForbidden

from school.models import Notification


def add_active_page(request):
    print(f"Current URL Name: {request.resolver_match.url_name}")
    return {'active_page': request.resolver_match.url_name}


def notification_context_processor(request):
    unred_notif = 0
    unread_notification = None
    all_notifications = Notification.objects.all()
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
    else:
        unred_notif = 0

    # This part should not be reachable after the above return statements.
    return {
        'unread_notification_count': unred_notif,
        'notifications': notifications,
        'all_notifications': all_notifications
    }
