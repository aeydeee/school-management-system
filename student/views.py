from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from school.models import Notification
from student.forms import StudentForm, ParentForm
from student.models import Parent, Student
from utils.notification_utils import create_notification


# Create your views here.


def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)  # Include request.FILES for image upload
        parent_form = ParentForm(request.POST)

        if student_form.is_valid() and parent_form.is_valid():
            # Save the parent instance first
            parent = parent_form.save()

            # Save the student instance without committing to the database
            student = student_form.save(commit=False)

            # Assign the parent to the student
            student.parent = parent

            # Save the student instance
            student.save()

            create_notification(request.user, f'Added Student: {student.first_name} {student.last_name}')

            messages.success(request, 'Student added successfully!')
            return HttpResponseRedirect(reverse('student_list'))

        else:
            # Show validation errors in the messages
            messages.error(request, 'Please correct the errors below.')

    else:
        # Initialize empty forms for GET requests
        student_form = StudentForm()
        parent_form = ParentForm()

    print(student_form.errors)
    print(parent_form.errors)

    return render(request, 'students/add-student.html', {
        'student_form': student_form,
        'parent_form': parent_form,
    })


def student_list(request):
    stud_list = Student.objects.select_related('parent').all()
    context = {
        'student_list': stud_list
    }
    return render(request, 'students/students.html', context)


def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    parent = student.parent

    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES,
                                   instance=student)  # Include request.FILES for image upload
        parent_form = ParentForm(request.POST, instance=parent)

        if student_form.is_valid() and parent_form.is_valid():
            # Save the parent instance first
            parent = parent_form.save()

            # Save the student instance without committing to the database
            student = student_form.save(commit=False)

            # Assign the parent to the student
            student.parent = parent

            # Save the student instance
            student.save()

            create_notification(request.user, f'Edited Student: {student.first_name} {student.last_name}')

            messages.success(request, 'Student edited successfully!')
            return HttpResponseRedirect(reverse('student_list'))

        else:
            # Show validation errors in the messages
            messages.error(request, 'Please correct the errors below.')
    else:
        student_form = StudentForm(instance=student)  # Include request.FILES for image upload
        parent_form = ParentForm(instance=parent)  # Include request.FILES for image upload
    return render(request, 'students/edit-student.html', {
        'student_form': student_form,
        'parent_form': parent_form
    })


def view_student(request, slug):
    student = get_object_or_404(Student, student_id=slug)
    return render(request, 'students/student-details.html', {
        'student': student
    })


def delete_student(request, slug):
    if request.method == 'POST':
        student = get_object_or_404(Student, slug=slug)
        student_name = f'{student.first_name} {student.last_name}'
        student.delete()

        create_notification(request.user, f'Deleted Student: {student_name}')

        return redirect('student_list')
    return HttpResponseForbidden()
