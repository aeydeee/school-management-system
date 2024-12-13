from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View

from class_group.forms import ClassForm, SectionForm
from class_group.models import Class, Section


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


class ClassUpdateView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'class_groups/edit-class.html'
    success_url = reverse_lazy('class:class_list')


class SectionManageView(View):
    template_name = 'class_groups/section/sections.html'

    def get(self, request, *args, **kwargs):
        sections = Section.objects.order_by('grade_level', 'name')
        form = SectionForm()
        return render(request, self.template_name, {'sections': sections, 'form': form})

    def post(self, request, *args, **kwargs):
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class:section_list')
        sections = Section.objects.order_by('grade_level', 'name')
        return render(request, self.template_name, {'sections': sections, 'form': form})


class SectionUpdateView(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'class_groups/section/edit-section.html'
    success_url = reverse_lazy('class:section_list')
