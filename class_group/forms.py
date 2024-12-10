from subject.models import Subject
from .models import Class, Section
from django import forms


class ClassForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),  # Replace with your model
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        empty_label="Select Subject",  # Optional
    )

    section = forms.ModelChoiceField(
        queryset=Section.objects.all(),  # Replace with your model
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        empty_label="Select Subject",  # Optional
    )

    class Meta:
        model = Class
        exclude = ['students']
        widgets = {

        }
