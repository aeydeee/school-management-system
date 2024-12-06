from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from department.forms import DepartmentForm
from department.models import Department


# Create your views here.
class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/departments.html'
    context_object_name = 'departments'
    ordering = ['-id']


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/add-department.html'
    success_url = reverse_lazy('department:department_list')


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/edit-department.html'
    success_url = reverse_lazy('department:department_list')

