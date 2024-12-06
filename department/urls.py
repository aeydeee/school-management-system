from django.urls import path

from department.views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView

app_name = 'department'

urlpatterns = [
    path('', DepartmentListView.as_view(), name='department_list'),
    path('add/', DepartmentCreateView.as_view(), name='add_department'),
    path('edit/<int:pk>/', DepartmentUpdateView.as_view(), name='edit_department'),

]
