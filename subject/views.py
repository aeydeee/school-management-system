from django.shortcuts import render
from django.views.generic import ListView

from subject.models import Subject


# Create your views here.
class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/subjects.html'
    context_object_name = 'subjects'
    ordering = ['-id']
