import secrets

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.http import request
from django.utils.crypto import get_random_string

from home_auth.models import CustomUser, PasswordResetRequest


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    role = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('others', 'Others')])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class': 'form-control',
        'placeholder': 'Username or Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True, label="Email Address")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract request from kwargs
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = CustomUser.objects.filter(email=email).first()
        # Example: Check if email exists in the database
        if user:
            token = secrets.token_urlsafe(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email(request=self.request)
            messages.success(self.request, 'Reset link sent to your email.')
        else:
            raise forms.ValidationError("No account found with this email address.")
        return email


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
