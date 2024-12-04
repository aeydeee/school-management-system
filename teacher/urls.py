from django.urls import path
from teacher import views
from teacher.views import TeacherListView, TeacherCreateView, TeacherDetailView, TeacherUpdateView, TeacherDeleteView

app_name = 'teacher'

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("teachers/", TeacherListView.as_view(), name='teacher_list'),
    path("view/<slug:slug>/", TeacherDetailView.as_view(), name="view_teacher"),
    path("add/", TeacherCreateView.as_view(), name='add_teacher'),
    path("edit/<slug:slug>/", TeacherUpdateView.as_view(), name='edit_teacher'),
    path("delete/<slug:slug>/", TeacherDeleteView.as_view(), name='delete_teacher'),
]
