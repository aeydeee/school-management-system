from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from class_group.forms import ClassForm
from class_group.models import Class


# Create your views here.
class ClassListView(ListView):
    model = Class
    template_name = 'class_groups/class_groups.html'
    context_object_name = 'class_groups'
    ordering = ['-id']


class ClassCreateView(CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'class_groups/add-class.html'
    success_url = reverse_lazy('class:class_list')
