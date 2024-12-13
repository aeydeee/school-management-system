from django.urls import path

from school import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student-dashboard/', views.dashboard, name='student_dashboard'),
    path('notification/mark-as-read/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('notification/clear-all/', views.clear_all_notification, name='clear_all_notification'),
]
