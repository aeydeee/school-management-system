from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from home_auth.forms import SignupForm, LoginForm, ForgotPasswordForm, PasswordResetForm
from home_auth.models import PasswordResetRequest, CustomUser


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, 'Signup Successfully!')
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'authentication/register.html', {
        'form': form,
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(password)
            try:
                user = authenticate(request, username=email_or_username, password=password)

                if user is not None:
                    user.backend = 'django.contrib.auth.backends.UsernameOrEmailBackend'
                    login(request, user)
                    messages.success(request, ' Login Successful')

                    if user.groups.filter(name='admin').exists():
                        return redirect('index')
                    elif user.groups.filter(name='student').exists():
                        return redirect('student_dashboard')
                    elif user.groups.filter(name='teacher').exists():
                        return redirect('teacher:dashboard')
                    else:
                        messages.error(request, 'Invalid user role')
                        return redirect('index')
                else:
                    messages.error(request, 'Invalid Credentials')

            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid Credentials')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {
        'form': form,
    })


def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST, request=request)

        if form.is_valid():
            email = form.cleaned_data['email']

            messages.success(request, 'Password reset link has been sent.')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = ForgotPasswordForm()

    return render(request, 'authentication/forgot-password.html', {
        'form': form
    })


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()

    if not reset_request.is_valid() or not reset_request:
        messages.error(request, 'Invalid or expired reset link')
        return redirect('index')

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            pw = form.cleaned_data['confirm_password']
            reset_request.user.set_password(pw)
            reset_request.user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'authentication/reset_password.html', {
        'form': form,
        'token': token
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')
