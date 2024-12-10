from django.urls import path

from class_group.views import ClassListView, ClassCreateView

app_name = 'class'

urlpatterns = [
    path('', ClassListView.as_view(), name='class_list'),
    path('add/', ClassCreateView.as_view(), name='add_class'),
]
