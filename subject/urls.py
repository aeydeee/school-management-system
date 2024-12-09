from django.urls import path

from subject.views import SubjectListView, SubjectCreateView, SubjectUpdateView

app_name = 'subject'

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_list'),
    path('add/', SubjectCreateView.as_view(), name='add_subject'),
    path('edit/<int:pk>/', SubjectUpdateView.as_view(), name='edit_subject'),
]
