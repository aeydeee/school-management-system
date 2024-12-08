from django.urls import path

from subject.views import SubjectListView

app_name = 'subject'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
]
