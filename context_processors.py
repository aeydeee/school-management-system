# context_processors.py
from django.http import JsonResponse, HttpResponseForbidden

from school.models import Notification


def add_active_page(request):
    return {'active_page': request.resolver_match.url_name}


def notification_context_processor(request):
    unread_notification = Notification.objects.filter(user=request.user, is_read=False)
    unred_notif = unread_notification.count()

    # This part should not be reachable after the above return statements.
    return {
        'unread_notification_count': unred_notif,
        'unread_notification': unread_notification
    }


