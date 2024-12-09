from django import forms

from department.models import Department
from subject.models import Subject


class SubjectForm(forms.ModelForm):
    code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),  # Replace with your model
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        empty_label="Select Department",  # Optional
    )

    class Meta:
        model = Subject
        fields = '__all__'
