from django.contrib import messages
from django.contrib.auth.models import Group
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView

from home_auth.forms import SignupForm, PasswordChangeForm, EditUserForm
from teacher.models import Teacher

from teacher.forms import TeacherForm, AddressForm
import logging

from utils.notification_utils import create_notification

logger = logging.getLogger(__name__)


# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teachers/teachers.html'


def dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')


class TeacherCreateView(View):
    template_name = 'teachers/add-teacher.html'
    success_url = reverse_lazy('teacher:teacher_list')

    def get(self, request, *args, **kwargs):
        context = {
            'teacher_form': TeacherForm(),
            'address_form': AddressForm(),
            'signup_form': SignupForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        teacher_form = TeacherForm(request.POST, request.FILES)
        address_form = AddressForm(request.POST)
        signup_form = SignupForm(request.POST)

        if all(form.is_valid() for form in [teacher_form, address_form, signup_form]):
            try:
                with transaction.atomic():
                    user = signup_form.save(commit=False)
                    address = address_form.save()
                    teacher = teacher_form.save(commit=False)

                    teacher.user = user
                    teacher.address = address
                    user.save()
                    teacher.save()

                    group, created = Group.objects.get_or_create(name='teacher')
                    user.groups.add(group)

                    create_notification(request.user, f'Added Teacher: {teacher.user.first_name}')
                    messages.success(request, 'Teacher created successfully!')
                    return redirect(self.success_url)
            except IntegrityError as e:
                logger.error(f"Database error: {e}")
                messages.error(request, 'An error occurred while creating the teacher.')
            except Exception as e:
                logger.exception(f"Unexpected error: {e}")
                messages.error(request, 'An unexpected error occurred.')

        else:
            messages.error(request, 'Please correct the errors below.')

        context = {
            'teacher_form': teacher_form,
            'address_form': address_form,
            'signup_form': signup_form,
        }

        return render(request, self.template_name, context)


class TeacherUpdateView(View):
    template_name = 'teachers/edit-teacher.html'
    success_url = reverse_lazy('teacher:teacher_list')

    def get(self, request, slug):
        teacher = get_object_or_404(Teacher, slug=slug)
        address = teacher.address
        user = teacher.user

        context = {
            'teacher_form': TeacherForm(instance=teacher),
            'address_form': AddressForm(instance=address),
            'signup_form': EditUserForm(instance=user),
            'reset_password_form': PasswordChangeForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        teacher = get_object_or_404(Teacher, slug=slug)
        address = teacher.address
        user = teacher.user

        teacher_form = TeacherForm(request.POST, request.FILES, instance=teacher)
        address_form = AddressForm(request.POST, instance=address)
        signup_form = EditUserForm(request.POST, instance=user)
        reset_password_form = PasswordChangeForm(request.POST)

        if all(form.is_valid() for form in [teacher_form, address_form, signup_form]):
            try:
                with transaction.atomic():
                    user = signup_form.save(commit=False)
                    address = address_form.save()
                    teacher = teacher_form.save(commit=False)

                    teacher.user = user
                    teacher.address = address

                    user.save()

                    if reset_password_form.is_valid():
                        new_password = reset_password_form.cleaned_data['confirm_password']
                        print(new_password)
                        user.set_password(new_password)
                        user.save()
                    else:
                        messages.error(request, "Password change form is invalid.")
                        return redirect('teacher:edit_teacher', slug=slug)

                    teacher.save()

                    group, created = Group.objects.get_or_create(name='teacher')
                    user.groups.add(group)

                    create_notification(request.user, f'Edited Teacher: {teacher.user.first_name}')
                    messages.success(request, 'Teacher edited successfully!')
                    return redirect(self.success_url)
            except IntegrityError as e:
                logger.error(f"Database error: {e}")
                messages.error(request, 'An error occurred while editing the teacher.')
            except Exception as e:
                logger.exception(f"Unexpected error: {e}")
                messages.error(request, 'An unexpected error occurred.')

        else:
            messages.error(request, 'Please correct the errors below.')

        context = {
            'teacher_form': teacher_form,
            'address_form': address_form,
            'signup_form': signup_form,
            'reset_password_form': reset_password_form,
        }
        return render(request, self.template_name, context)


class TeacherDeleteView(View):
    success_url = reverse_lazy('teacher:teacher_list')

    def post(self, request, slug):
        teacher = get_object_or_404(Teacher, slug=slug)
        user = teacher.user
        address = teacher.address

        try:
            with transaction.atomic():
                address.delete()
                teacher.delete()
                user.delete()

                create_notification(request.user, f'Deleted Teacher: {teacher.user.first_name}')
                messages.success(request, 'Teacher deleted successfully')
                return redirect(self.success_url)

        except IntegrityError as e:
            logger.error(f"Database error: {e}")
            messages.error(request, 'An error occurred while deleting the teacher.')

        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            messages.error(request, 'An unexpected error occurred.')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/teacher-details.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
