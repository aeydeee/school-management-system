from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render

from school.models import Notification


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def dashboard(request):
    return render(request, 'students/student-dashboard.html', {
    })


def mark_notification_as_read(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user, is_read=False)
        notification.update(is_read=True)
        print('Marking notification as read')
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()


def clear_all_notification(request):
    if request.method == 'POST':
        notification = Notification.objects.filter(user=request.user)
        notification.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()
