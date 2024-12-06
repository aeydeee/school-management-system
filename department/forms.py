from django import forms

from teacher.models import Teacher
from .models import Department


class DepartmentForm(forms.ModelForm):
    department_id = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )

    head_of_department = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),  # Replace with your model
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        empty_label="Select HOD",  # Optional
    )

    class Meta:
        model = Department
        fields = '__all__'
        widgets = {

        }
