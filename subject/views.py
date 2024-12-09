from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from subject.forms import SubjectForm
from subject.models import Subject


# Create your views here.
class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/subjects.html'
    context_object_name = 'subjects'
    ordering = ['-id']


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects/add-subject.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subject:subject_list')


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'subjects/edit-subject.html'
    success_url = reverse_lazy('subject:subject_list')
